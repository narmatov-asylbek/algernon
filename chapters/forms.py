
from django import forms
from django_quill.forms import QuillFormField, QuillWidget
from django.utils.translation import gettext_lazy as _


class AddChapterForm(forms.Form):
    title = forms.CharField(max_length=200, label=_("Title"), widget=forms.TextInput(attrs={
        'class': 'form_control'
    }))
    text = QuillFormField(label=_("Text"), widget=QuillWidget(attrs={
        'class': 'form_control quill_form',
        'cols': '20',
        'rows': '6'
    }))