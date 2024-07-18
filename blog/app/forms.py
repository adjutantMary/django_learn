from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, label='Ваше имя')
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)

# в чем разница между этими двумя формами.
# Form сам создает форму, указывая поля для формы
# ModelForm использует в качестве шаблона формы модель
# полем fields мы выбираем, какие поля модели хотим забрать
# полем exclude наоборот, какие поля мы не хотим забирать

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
    
