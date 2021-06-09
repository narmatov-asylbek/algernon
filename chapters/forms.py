
from django import forms
from .models import Chapter
from django_quill.forms import QuillFormField, QuillWidget
from django.utils.translation import gettext_lazy as _


class ChapterForm(forms.ModelForm):
    status = forms.CheckboxInput()
    class Meta:
        model = Chapter
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input'
            })
        }