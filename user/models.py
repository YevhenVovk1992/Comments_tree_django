from django.contrib.auth.models import User
from django.db import models

from utils.ChangeFile import ImageEditor


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', unique=True, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_images',  blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()
        if self.avatar:
            ImageEditor.reduce_image(self.avatar.path, 240, 160)
