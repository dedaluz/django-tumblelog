import fnmatch
import re
from urllib2 import HTTPError, URLError

from south.modelsinspector import add_introspection_rules

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.fields import NOT_PROVIDED
from django.utils.translation import ugettext as _


class OEmbedURLField(models.URLField):
    """
    A subclass of URLField to ensure that the value points to a valid resource
    on the defined oEmbed provider.
    """

    def validate(self, value, model_instance):
        """
        Adds two methods of validation:
        1) That the field's value matches the defined schemas.
        2) That the field's value points to a valid resource on the provider
        """
        self.validate_match(value, model_instance)
        self.validate_response(value, model_instance)
        super(OEmbedURLField, self).validate(value, model_instance)

    def validate_match(self, value, model_instance):
        """
        Validation method to ensure that the field's value matches one of the
        resource patterns defined by the model instance's
        TumblelogMeta.oembed_schema list.
        """
        object_name = model_instance._meta.verbose_name
        match = False
        for pattern in model_instance.oembed_schema:
            regex_pattern = fnmatch.translate(pattern)
            if re.match(regex_pattern, value):
                match = True
                break
        if not match:
            raise ValidationError(
                _('Invalid %s URL') % object_name
            )

    def validate_response(self, value, model_instance):
        """
        Validation method to ensure that the provider's response is valid for
        the given resource.

        The oEmbed 1.0 spec permits three classes of errors:
        - 404 if the provider has no resource for the requested url
        - 401 if the specified URL contains a private (non-public) resource
        - 501 if the provider cannot return a response in the requested format

        Though all HTTP errors are raised, friendly error messages are only
        provided for each of these permitted scenarios.
        """

        object_name = model_instance._meta.verbose_name
        try:
            model_instance.oembed_retrieve(suppress_http_errors=False)
        except HTTPError, e:
            if e.code == 404:
                message = _('%s not found' % object_name)
            elif e.code == 401:
                message = _((
                    'This %s is marked as private; you should link to it '
                    'directly to allow the provider to regulate access control'
                ) % object_name)
            elif e.code == 501:
                message = _(
                    '%s not available in the requested format' % object_name
                )
            else:
                message = _(e.msg)
            raise ValidationError(message)
        except URLError:
            raise ValidationError(_('Unable to contact server'))


add_introspection_rules([
    (
        [OEmbedURLField],
        [],
        {
            'null': ['null', {'default': False}],
            'blank': ['blank', {'default': False, 'ignore_if':'primary_key'}],
            'primary_key': ['primary_key', {'default': False}],
            'max_length': ['max_length', {'default': None}],
            'unique': ['_unique', {'default': False}],
            'db_index': ['db_index', {'default': False}],
            'default': ['default', {
                'default': NOT_PROVIDED,
                'ignore_dynamics': True
            }],
            'db_column': ['db_column', {'default': None}],
            'db_tablespace': ['db_tablespace', {
                'default': settings.DEFAULT_INDEX_TABLESPACE
            }],
        },
    ),
], ['^tumblelog\.fields\.OEmbedURLField'])
