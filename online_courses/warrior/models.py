from PIL import Image
from cloudinary.models import CloudinaryField
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
    avatar = CloudinaryField('avatar', blank=True, null=True)

    def __str__(self):
        return self.war_nik

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)