from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(blank=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    post_title = models.CharField(max_length=50)
    description = models.TextField(default="text")
    datetime = models.DateTimeField(auto_now_add=True)
    updatedatetime = models.DateTimeField(auto_now=True)

