import os

AWS_USERNAME = "vdhug"
AWS_ACCESS_KEY_ID = "AKIATW2DS46QKSRDU4VO"
AWS_SECRET_ACCESS_KEY = "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"
AWS_DEFAULT_ACL = None
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'airline.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'airline.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'medium-django-s3-storage'
S3DIRECT_REGION = 'sa-east-1'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME

MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

AWS_HEADERS = {
    'Cache-Control': 'max-age=86400',
}
