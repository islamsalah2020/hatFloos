from django import forms

from .models import Project, Category


class ProjectCreationForm(forms.ModelForm):
    # creator = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Project
        fields = ['title', 'description', 'category', 'target', 'start_date', 'end_date', 'creator']


class CatCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
