from django.db import models

from accounts.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(db_index=True, unique=True, max_length=255)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(blank=True, max_length=400)
    body = RichTextUploadingField()
    image = models.ImageField(upload_to='featured_image', blank=True)

    def __str__(self):
        return self.title
