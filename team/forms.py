from django import forms
from .models import FileUpload
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file']
