from django import forms

from books.models import Book, Cycle


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['cover', 'title', 'type', 'genre', 'cycle', 'description', 'remark',
                  'is_introductory', 'is_eighteen_plus', 'can_comment', 'can_read', 'can_download']

        labels = {
            'cover': 'Обложка',
            'title': 'Название произведения',
            'type': 'Форма произведения',
            'genre': 'Жанр произведения',
            'cycle': 'Цикл',
            'description': 'Аннотация',
            'remark': 'Примечания автора',
            'is_introductory': 'Ознакомительный фрагмент',
            'is_eighteen_plus': 'Для взрослых (+18)',
            'can_comment': 'Кто может комментировать',
            'can_read': 'Кто может читать',
            'can_download': 'Кто может скачивать'
        }
        widgets = {
            'cover': forms.FileInput(attrs={
                'class': "button"
            }),
            'title': forms.TextInput(attrs={
                'class': 'input'
            }),
            'type': forms.Select(attrs={
                'class': 'select'
            }),
            'genre': forms.Select(attrs={
                'class': 'select'
            }),
            'cycle': forms.Select(attrs={
                'class': 'select'
            }),
            'description': forms.Textarea(attrs={
                'class': 'textarea',
                'cols': '20',
                'rows': '6'
            }),
            'remark': forms.Textarea(attrs={
                'class': 'textarea',
                'cols': '20',
                'rows': '3'
            }),
            'can_read': forms.Select(attrs={
                'class': 'select'
            }),
            'can_download': forms.Select(attrs={
                'class': 'select'
            }),
            'can_comment': forms.Select(attrs={
                'class': 'select'
            }),
        }


class CycleForm(forms.ModelForm):
    class Meta:
        model = Cycle
        fields = ['name', 'desciption', 'is_finished']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'desciption': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': '20',
                'rows': '6'
            }),
        }
        labels = {
            'name': 'Название Цикла',
            'desciption': 'Описание',
            'is_finished': 'Цикл завершен'
        }