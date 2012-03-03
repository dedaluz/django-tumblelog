STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
)

SOUNDCLOUD_HEIGHT_CHOICES = (
    ('81', 'Compact (81px)',),
    ('305', 'Normal (305px)',),
)

# Flickr claims to support up to 1024x1024, but the 1024 size appears to be
# returning 500x500, so it has been commented out for the time being.
FLICKR_SIZE_CHOICES = (
    # ('1024', 'Large (1024px max)'),
    ('640', 'Large (640px)'),
    ('500', 'Medium (500px)'),
    ('240', 'Small (240px)'),
    ('100', 'Thumbnail (100px)'),
    ('75', 'Square (75x75)'),
)

TWITTER_LANGUAGE_CHOICES = (
    ('zh-cn', 'Chinese (Simplified)'),
    ('zh-tw', 'Chinese (Traditional)'),
    ('da', 'Danish'),
    ('nl', 'Dutch'),
    ('en', 'English'),
    ('fil', 'Filipino'),
    ('fi', 'Finnish'),
    ('fr', 'French'),
    ('de', 'German'),
    ('hi', 'Hindi'),
    ('id', 'Indonesian'),
    ('it', 'Italian'),
    ('ja', 'Japanese'),
    ('ko', 'Korean'),
    ('msa', 'Malay'),
    ('no', 'Norwegian'),
    ('pl', 'Polish'),
    ('pt', 'Portuguese'),
    ('ru', 'Russian'),
    ('es', 'Spanish'),
    ('sv', 'Swedish'),
    ('tr', 'Turkish'),
)
