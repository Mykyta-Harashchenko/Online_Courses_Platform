from django import forms
from django.forms import ImageField, FileInput

from .models import Warrior

class WarriorForm(forms.ModelForm):
    avatar = ImageField(widget=FileInput())
    class Meta:
        model = Warrior
        fields = ['first_name',
                  'second_name',
                  'war_nik',
                  'wound_type',
                  'wound_location',
                  'wound_case',
                  'wound_date',
                  'sum_amount',
                  'avatar']