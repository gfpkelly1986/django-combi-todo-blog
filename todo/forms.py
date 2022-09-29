from .models import Comment
from .models import Item
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']
