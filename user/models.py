from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', unique=True, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_images',  blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()
        try:
            img = Image.open(self.avatar.path)
        except ValueError:
            pass
        else:
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
            img.save(self.avatar.path)