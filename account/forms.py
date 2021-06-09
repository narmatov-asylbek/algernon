from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import Contact, CustomUser


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input'
    }))


class SettingsForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['image', 'username', 'slug',
                  'name', 'status', 'birthday',
                  'birthday_visibility', 'gender',
                  'information']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': "button"
            }),
            'username': forms.TextInput(attrs={
                'class': 'input'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'input'
            }),
            'name': forms.TextInput(attrs={
                'class': 'input'
            }),
            'status': forms.TextInput(attrs={
                'class': 'input'
            }),
            'birthday': forms.DateInput(attrs={
                'class': 'input'
            }),
            'birthday_visibility': forms.Select(attrs={
                'class': 'select'
            }),
            'gender': forms.Select(attrs={
                'class': 'select'
            }),
            'information': forms.Textarea(attrs={
                'class': 'textarea',
                'cols': '20',
                'rows': '6'
            })
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['website', 'twitter',
                  'vk', 'facebook', 'instagram']
        widgets = {
            'website': forms.URLInput(attrs={
                'class': 'input'
            }),
            'twitter': forms.URLInput(attrs={
                'class': 'input'
            }),
            'vk': forms.URLInput(attrs={
                'class': 'input'
            }),
            'facebook': forms.URLInput(attrs={
                'class': 'input'
            }),
            'instagram': forms.URLInput(attrs={
                'class': 'input'
            }),
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input'

    def clean_name(self):
        name = self.cleaned_data['name']
        if CustomUser.objects.filter(name=name).exists():
            raise ValidationError('Данное имя пользователя уже занято')
        return name