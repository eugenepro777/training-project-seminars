import datetime
from django import forms
from .models import Author


class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=40, label='Имя')
    last_name = forms.CharField(max_length=40, label='Фамилия')
    email = forms.EmailField(label='Электронная почта')
    bio = forms.CharField(widget=forms.Textarea, label='Биография')
    birth_date = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Дата рождения'
    )


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=40, label='Название статьи')
    body = forms.CharField(widget=forms.Textarea, label='Текст статьи')
    date = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control',
                                                                                      'type': 'date'}))
    author = forms.ModelChoiceField(Author.objects.all().order_by('?'), label='Автор')
    category = forms.CharField(max_length=40, label='Категория')
    views_count = forms.IntegerField(initial=0, label='Количество просмотров')
    pub_flag = forms.BooleanField(required=False, label='Опубликована')
