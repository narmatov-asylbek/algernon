from django import forms

from .models import Contact, CustomUser


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class SettingsForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['image', 'pseudonym', 'slug',
                  'name', 'status', 'birthday',
                  'birthday_visibility', 'gender',
                  'information']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['website', 'twitter',
                  'vk', 'facebook', 'instagram']


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'pseudonym', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }