
from django import forms
from .models import Chapter
from django_quill.forms import QuillFormField, QuillWidget
from django.utils.translation import gettext_lazy as _


class ChapterForm(forms.ModelForm):

    class Meta:
        model = Chapter
        fields = ['title', 'text', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input'
            }),
            'status': forms.CheckboxInput(attrs={
                'class': 'checkbox'
            })
        }