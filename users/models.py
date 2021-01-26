from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(default='john_doe@email.com', max_length=254)
    date_of_birth = models.CharField(
        default='05/25/2015', null=False, max_length=30)
