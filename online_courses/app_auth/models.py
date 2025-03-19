from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


def get_default_avatar():
    return 'https://res.cloudinary.com/crowdfundingplatform/image/upload/v1741871751/default_avatar_neb9hb.png'
# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = CloudinaryField('avatar', blank=True, null=True, default=get_default_avatar)

    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)