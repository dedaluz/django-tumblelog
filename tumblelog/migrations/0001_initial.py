# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Post'
        db.create_table('tumblelog_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='d', max_length=1)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('post_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64, db_index=True)),
        ))
        db.send_create_signal('tumblelog', ['Post'])

        # Adding model 'Rdio'
        db.create_table('tumblelog_rdio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='d', max_length=1)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64, db_index=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('provider_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('provider_url', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('cache_age', self.gf('django.db.models.fields.IntegerField')(default=86400)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('embed', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('rdio_url', self.gf('tumblelog.fields.OEmbedURLField')(max_length=1024)),
            ('rdio_title', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('thumbnail_url', self.gf('django.db.models.fields.URLField')(max_length=1024, null=True, blank=True)),
            ('thumbnail_width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('thumbnail_height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('tumblelog', ['Rdio'])

        # Adding model 'SoundCloud'
        db.create_table('tumblelog_soundcloud', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='d', max_length=1)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64, db_index=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('provider_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('provider_url', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('cache_age', self.gf('django.db.models.fields.IntegerField')(default=86400)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('embed', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('soundcloud_url', self.gf('tumblelog.fields.OEmbedURLField')(max_length=1024)),
            ('soundcloud_title', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('soundcloud_description', self.gf('django.db.models.fields.CharField')(max_length=8192, null=True, blank=True)),
            ('maxwidth', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True)),
            ('maxheight', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(default='', max_length=6, null=True, blank=True)),
            ('auto_play', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('show_comments', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('html5_player', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('tumblelog', ['SoundCloud'])

        # Adding model 'Gist'
        db.create_table('tumblelog_gist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='d', max_length=1)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64, db_index=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('provider_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('provider_url', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('cache_age', self.gf('django.db.models.fields.IntegerField')(default=86400)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('embed', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('gist_url', self.gf('tumblelog.fields.OEmbedURLField')(max_length=1024)),
            ('git_user', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('git_user_url', self.gf('django.db.models.fields.URLField')(max_length=512)),
            ('gist_title', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('tumblelog', ['Gist'])

        # Adding model 'File'
        db.create_table('tumblelog_file', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='d', max_length=1)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64, db_index=True)),
            ('file_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('file_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('tumblelog', ['File'])

        # Adding model 'Link'
        db.create_table('tumblelog_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='d', max_length=1)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64, db_index=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('link_text', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('tumblelog', ['Link'])

        # Adding model 'Image'
        db.create_table('tumblelog_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='d', max_length=1)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64, db_index=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('tumblelog', ['Image'])

        # Adding model 'Flickr'
        db.create_table('tumblelog_flickr', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='d', max_length=1)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64, db_index=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('provider_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('provider_url', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('cache_age', self.gf('django.db.models.fields.IntegerField')(default=86400)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('flickr_url', self.gf('tumblelog.fields.OEmbedURLField')(max_length=1024)),
            ('flickr_user', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('flickr_user_url', self.gf('django.db.models.fields.URLField')(max_length=1024, null=True, blank=True)),
            ('flickr_title', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('size', self.gf('django.db.models.fields.CharField')(default=640, max_length=4)),
        ))
        db.send_create_signal('tumblelog', ['Flickr'])

        # Adding model 'Instagram'
        db.create_table('tumblelog_instagram', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='d', max_length=1)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64, db_index=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('provider_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('provider_url', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('cache_age', self.gf('django.db.models.fields.IntegerField')(default=86400)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('instagram_url', self.gf('tumblelog.fields.OEmbedURLField')(max_length=1024)),
            ('instagram_user', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('instagram_title', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('tumblelog', ['Instagram'])

        # Adding model 'Text'
        db.create_table('tumblelog_text', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='d', max_length=1)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64, db_index=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('tumblelog', ['Text'])

        # Adding model 'Article'
        db.create_table('tumblelog_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='d', max_length=1)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64, db_index=True)),
            ('excerpt', self.gf('django.db.models.fields.TextField')()),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('tumblelog', ['Article'])

        # Adding model 'Tweet'
        db.create_table('tumblelog_tweet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='d', max_length=1)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64, db_index=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('provider_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('provider_url', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('cache_age', self.gf('django.db.models.fields.IntegerField')(default=86400)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('embed', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('tweet_url', self.gf('tumblelog.fields.OEmbedURLField')(max_length=1024)),
            ('hide_media', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hide_thread', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('maxwidth', self.gf('django.db.models.fields.IntegerField')(default=325, max_length=3)),
            ('language', self.gf('django.db.models.fields.CharField')(default='en', max_length=2)),
            ('twitter_user', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('twitter_user_url', self.gf('django.db.models.fields.URLField')(max_length=512)),
        ))
        db.send_create_signal('tumblelog', ['Tweet'])

        # Adding model 'YouTube'
        db.create_table('tumblelog_youtube', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='d', max_length=1)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64, db_index=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('provider_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('provider_url', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('cache_age', self.gf('django.db.models.fields.IntegerField')(default=86400)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('embed', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('thumbnail_url', self.gf('django.db.models.fields.URLField')(max_length=1024, null=True, blank=True)),
            ('thumbnail_width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('thumbnail_height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('youtube_url', self.gf('tumblelog.fields.OEmbedURLField')(max_length=1024)),
            ('youtube_user', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('youtube_user_url', self.gf('django.db.models.fields.URLField')(max_length=1024, null=True, blank=True)),
            ('youtube_title', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
        ))
        db.send_create_signal('tumblelog', ['YouTube'])

        # Adding model 'Vimeo'
        db.create_table('tumblelog_vimeo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='d', max_length=1)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64, db_index=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('provider_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('provider_url', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('cache_age', self.gf('django.db.models.fields.IntegerField')(default=86400)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('embed', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('thumbnail_url', self.gf('django.db.models.fields.URLField')(max_length=1024, null=True, blank=True)),
            ('thumbnail_width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('thumbnail_height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('vimeo_url', self.gf('tumblelog.fields.OEmbedURLField')(max_length=1024)),
            ('vimeo_user', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('vimeo_user_url', self.gf('django.db.models.fields.URLField')(max_length=1024, null=True, blank=True)),
            ('vimeo_title', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('vimeo_video_id', self.gf('django.db.models.fields.IntegerField')(max_length=9, null=True, blank=True)),
            ('duration', self.gf('django.db.models.fields.IntegerField')(max_length=6, null=True, blank=True)),
        ))
        db.send_create_signal('tumblelog', ['Vimeo'])


    def backwards(self, orm):
        
        # Deleting model 'Post'
        db.delete_table('tumblelog_post')

        # Deleting model 'Rdio'
        db.delete_table('tumblelog_rdio')

        # Deleting model 'SoundCloud'
        db.delete_table('tumblelog_soundcloud')

        # Deleting model 'Gist'
        db.delete_table('tumblelog_gist')

        # Deleting model 'File'
        db.delete_table('tumblelog_file')

        # Deleting model 'Link'
        db.delete_table('tumblelog_link')

        # Deleting model 'Image'
        db.delete_table('tumblelog_image')

        # Deleting model 'Flickr'
        db.delete_table('tumblelog_flickr')

        # Deleting model 'Instagram'
        db.delete_table('tumblelog_instagram')

        # Deleting model 'Text'
        db.delete_table('tumblelog_text')

        # Deleting model 'Article'
        db.delete_table('tumblelog_article')

        # Deleting model 'Tweet'
        db.delete_table('tumblelog_tweet')

        # Deleting model 'YouTube'
        db.delete_table('tumblelog_youtube')

        # Deleting model 'Vimeo'
        db.delete_table('tumblelog_vimeo')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tumblelog.article': {
            'Meta': {'object_name': 'Article'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'excerpt': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'tumblelog.file': {
            'Meta': {'object_name': 'File'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'tumblelog.flickr': {
            'Meta': {'object_name': 'Flickr'},
            'cache_age': ('django.db.models.fields.IntegerField', [], {'default': '86400'}),
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'flickr_title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'flickr_url': ('tumblelog.fields.OEmbedURLField', [], {'max_length': '1024'}),
            'flickr_user': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'flickr_user_url': ('django.db.models.fields.URLField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'provider_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'provider_url': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'default': '640', 'max_length': '4'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'tumblelog.gist': {
            'Meta': {'object_name': 'Gist'},
            'cache_age': ('django.db.models.fields.IntegerField', [], {'default': '86400'}),
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'embed': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'gist_title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'gist_url': ('tumblelog.fields.OEmbedURLField', [], {'max_length': '1024'}),
            'git_user': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'git_user_url': ('django.db.models.fields.URLField', [], {'max_length': '512'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provider_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'provider_url': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'tumblelog.image': {
            'Meta': {'object_name': 'Image'},
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'tumblelog.instagram': {
            'Meta': {'object_name': 'Instagram'},
            'cache_age': ('django.db.models.fields.IntegerField', [], {'default': '86400'}),
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'instagram_title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'instagram_url': ('tumblelog.fields.OEmbedURLField', [], {'max_length': '1024'}),
            'instagram_user': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'provider_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'provider_url': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'tumblelog.link': {
            'Meta': {'object_name': 'Link'},
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'tumblelog.post': {
            'Meta': {'ordering': "['-date_published']", 'object_name': 'Post'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'post_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'})
        },
        'tumblelog.rdio': {
            'Meta': {'object_name': 'Rdio'},
            'cache_age': ('django.db.models.fields.IntegerField', [], {'default': '86400'}),
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'embed': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provider_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'provider_url': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'rdio_title': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'rdio_url': ('tumblelog.fields.OEmbedURLField', [], {'max_length': '1024'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            'thumbnail_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'thumbnail_url': ('django.db.models.fields.URLField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'thumbnail_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'tumblelog.soundcloud': {
            'Meta': {'object_name': 'SoundCloud'},
            'auto_play': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cache_age': ('django.db.models.fields.IntegerField', [], {'default': '86400'}),
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'embed': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'html5_player': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxheight': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'maxwidth': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'provider_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'provider_url': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'show_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'soundcloud_description': ('django.db.models.fields.CharField', [], {'max_length': '8192', 'null': 'True', 'blank': 'True'}),
            'soundcloud_title': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'soundcloud_url': ('tumblelog.fields.OEmbedURLField', [], {'max_length': '1024'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'tumblelog.text': {
            'Meta': {'object_name': 'Text'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'tumblelog.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'cache_age': ('django.db.models.fields.IntegerField', [], {'default': '86400'}),
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'embed': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hide_media': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hide_thread': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            'maxwidth': ('django.db.models.fields.IntegerField', [], {'default': '325', 'max_length': '3'}),
            'provider_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'provider_url': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'tweet_url': ('tumblelog.fields.OEmbedURLField', [], {'max_length': '1024'}),
            'twitter_user': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'twitter_user_url': ('django.db.models.fields.URLField', [], {'max_length': '512'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'tumblelog.vimeo': {
            'Meta': {'object_name': 'Vimeo'},
            'cache_age': ('django.db.models.fields.IntegerField', [], {'default': '86400'}),
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'embed': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provider_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'provider_url': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            'thumbnail_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'thumbnail_url': ('django.db.models.fields.URLField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'thumbnail_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'vimeo_title': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'vimeo_url': ('tumblelog.fields.OEmbedURLField', [], {'max_length': '1024'}),
            'vimeo_user': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'vimeo_user_url': ('django.db.models.fields.URLField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'vimeo_video_id': ('django.db.models.fields.IntegerField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'tumblelog.youtube': {
            'Meta': {'object_name': 'YouTube'},
            'cache_age': ('django.db.models.fields.IntegerField', [], {'default': '86400'}),
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'embed': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provider_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'provider_url': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            'thumbnail_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'thumbnail_url': ('django.db.models.fields.URLField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'thumbnail_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'youtube_title': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'youtube_url': ('tumblelog.fields.OEmbedURLField', [], {'max_length': '1024'}),
            'youtube_user': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'youtube_user_url': ('django.db.models.fields.URLField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tumblelog']
