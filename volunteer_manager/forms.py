from django import forms
from django.contrib.auth.models import User
from .models import Volunteer

class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User  # Associate the form with the User model
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        # Save the User instance
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['phone_number', 'skills']
