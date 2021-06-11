from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    """ Form for creating new Review """
    class Meta:
        model = Review
        fields = ['content']