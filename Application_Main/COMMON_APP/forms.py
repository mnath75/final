from dataclasses import fields
from xml.parsers.expat import model
from django.forms import ModelForm
from .models import Article
  

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

