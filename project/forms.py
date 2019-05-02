from django.forms import ModelForm
from django import forms
from django.db import models
from .models import Project, Category, Pic


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'category', 'target', 'start_date', 'end_date']


class PictureCreationForm(ModelForm):
    pic = forms.ImageField(label='Image')

    class Meta:
        model = Pic
        fields = ['pic']


class CatCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class TagForm(forms.Form):
    tag = forms.CharField(max_length=10)
