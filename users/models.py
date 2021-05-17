from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    character_img = models.ImageField(null=True, upload_to='uploads/', height_field=None, width_field=None, max_length=100);
    xp = models.PositiveIntegerField(default=0)
    lvl = models.PositiveSmallIntegerField(default=1)
    email = models.CharField(max_length=200, unique=True)