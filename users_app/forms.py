from django import forms
from .models import Student


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'roll', 'semester']






