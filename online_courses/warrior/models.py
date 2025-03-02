from PIL import Image
from django.contrib.auth.models import User
from django.db import models


class Warrior(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    first_name = models.TextField()
    second_name = models.TextField()
    war_nik = models.TextField()
    wound_type = models.TextField()
    wound_case = models.TextField()
    wound_location = models.TextField()
    wound_date = models.TextField()
    sum_amount = models.IntegerField()
    sum_raised = models.IntegerField(default=0)
    avatar = models.ImageField(default='default_avatar.png', upload_to='profile_images')

    def __str__(self):
        return self.war_nik

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 250 or img.width > 250:
            new_img = (250, 250)
            img.thumbnail(new_img)
            img.save(self.avatar.path)