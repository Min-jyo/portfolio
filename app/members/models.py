from django.conf import settings
from django.db import models

# Create your models here.

class User(models.Model):
    author = models.CharField(max_length=4)
    age = models.IntegerField()
    email = models.EmailField()
    major = models.CharField(max_length=10)
    marital_status = models.BooleanField()
    core_strength = models.TextField()
    career = models.TextField()
    img_profile = models.ImageField(blank=True)

    def __str__(self):
        return self.author