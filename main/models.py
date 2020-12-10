from django.db import models
import os
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{:%Y-%m-%d-%H-%M-%S}.{}'.format(datetime.now(), ext)
    return os.path.join('./static/uploads', filename)


def file_size_limit(value):
    limit = 2*1024*1024
    if value.size >= limit:
        raise ValidationError(_('File size must be lower than 2 mb'))


class MakePost(models.Model):
    post_title = models.CharField(max_length=100)
    post_text = models.TextField()
    post_img = models.ImageField(upload_to=content_file_name, validators=[file_size_limit])
    post_user = models.CharField(max_length=50)

