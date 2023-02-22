from django.forms import ModelForm
from django import forms
from .models import Song
 
class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'