from django.forms import ModelForm, forms
from django.db import models
from .models import Project, Category, CustomUser


class ProjectCreationForm(ModelForm):
    # title = forms.CharField(max_length=20)
    # description = forms.CharField(max_length=20)
    # category = forms.CharField(max_length=20)
    # target = forms.IntegerField()
    # start_date = forms.DateTimeField(required=False)
    # end_date = forms.DateTimeField(required=False)
    # creator = forms.CharField(max_length=20)
    class Meta:
        model = Project
        fields = ['title', 'description', 'category', 'target', 'start_date', 'end_date', 'creator']


class CatCreationForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
