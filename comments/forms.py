from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """ Form for creating comments """
    class Meta:
        model = Comment
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.Textarea(attrs={
                'class': 'textarea',
                'placeholder': "Добавить комментарий",
                'rows': '3'
            })
        }