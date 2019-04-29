from django.forms import ModelForm

from .models import Project, Category

class ProjectCreationForm(ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'description', 'category', 'target', 'start_date', 'end_date','creator']


class CatCreationForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
