from django.shortcuts import render , HttpResponse
from .models import Category
from project.forms import ProjectCreationForm, CatCreationForm


def create(request):
    if request.method == 'POST':
        form = ProjectCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form2 = CatCreationForm()
            args = {'form': form2}
            return render(request, 'project/index.html', args)
    else:
        form = ProjectCreationForm()
        args = {'form': form}
        return render(request, 'project/CreateProject.html', args)


def create_cat(request):
    if request.method == 'POST':
        form = CatCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form2 = ProjectCreationForm()
            args = {'form': form2}
            return render(request, 'project/CreateProject.html', args)
    else:
        form = CatCreationForm()
        args = {'form': form}
        return render(request, 'project/CreateCat.html', args)

