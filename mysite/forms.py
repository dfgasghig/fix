from django import forms
from .models import Post, Category, Review, RATE_CHOICES

try:
    class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('title', 'author', 'category', 'tags', 'body')
            widgets = {
                'title': forms.TextInput(attrs = {'class': 'form-control'}),
                'author': forms.TextInput(attrs = {'class': 'form-control', 'value': '', 'id': 'id_token', 'type': 'hidden'}),
                'category': forms.Select(choices = Category.objects.all().values_list('name', 'name'), attrs = {'class': 'form-control'}),
                'tags': forms.TextInput(attrs = {'class': 'form-control'}),
                'body': forms.Textarea(attrs = {'class': 'form-control'}),
            }
except Exception:
    class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('title', 'author', 'category', 'tags', 'body')
            widgets = {
                'title': forms.TextInput(attrs = {'class': 'form-control'}),
                'author': forms.TextInput(attrs = {'class': 'form-control', 'value': '', 'id': 'id_token', 'type': 'hidden'}),
                'category': forms.Select(attrs = {'class': 'form-control'}),
                'tags': forms.TextInput(attrs = {'class': 'form-control'}),
                'body': forms.Textarea(attrs = {'class': 'form-control'}),
            }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tags', 'body')
        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
            'tags': forms.TextInput(attrs = {'class': 'form-control'}),
            'body': forms.Textarea(attrs = {'class': 'form-control'}),
        }

class RateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text', 'rate')
        widget = {
            'text': forms.Textarea(attrs = {'class': 'form-control'}),
            'rate': forms.Select(choices = RATE_CHOICES, attrs = {'class': 'form-control'}),
        }
