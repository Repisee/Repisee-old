from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    discription = models.TextField()
    date_of_post = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(null=True, blank=True)
