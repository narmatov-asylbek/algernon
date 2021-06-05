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
        widgets = {
            'image': forms.FileInput(attrs={
                'class': "button"
            }),
            'pseudonym': forms.TextInput(attrs={
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




class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'pseudonym', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input'