# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#
# from .models import Project
#
#
# class CustomUserCreationForm(UserCreationForm):
#     title = forms.CharField(max_length=20)
#     description = forms.CharField(max_length=20)
#     category = forms.CharField(max_length=20)
#     target = forms.IntegerField()
#     start_date = forms.DateTimeField(required=False)
#     end_date = forms.DateTimeField(required=False)
#     creator = forms.CharField(max_length=11)
#
#     class Meta(UserCreationForm):
#         model = Project
#
#         fields = (
#             'username', 'title', 'description', 'category', 'target', 'start_date', 'end_date', 'creator')

from django.forms import ModelForm

from .models import Project, Category


class ProjectCreationForm(ModelForm):
    # title = forms.CharField(max_length=20)
    # description = forms.CharField(max_length=20)
    # category = forms.CharField(max_length=20)
    # target = forms.IntegerField()
    # start_date = forms.DateTimeField(required=False)
    # end_date = forms.DateTimeField(required=False)
    # creator = forms.CharField(max_length=11)

    class Meta:
        model = Project
        fields = ['title', 'description', 'category', 'target', 'start_date','end_date', 'creator']


class CatCreationForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name']

