from django.shortcuts import redirect,render, HttpResponse
from .models import Category, CustomUser, Project, Donation
from django.db.models import Sum
from project.forms import ProjectCreationForm, CatCreationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/users/login')  # redirect when user is not logged in
def create(request, uid):
    if request.method == 'POST':

        # request.POST.creator_id = uid
        # print("------------------------------------------------------")
        # print(request.POST.creator_id)
        # print("------------------------------------------------------")
        # print(request.POST)
        # print("------------------------------------------------------")

        form = ProjectCreationForm(request.POST)
        if form.is_valid():
            form.save()
            projects = Project.objects.filter(creator_id=uid)
            my_projects = []
            for project in projects:
                total_donation = Donation.objects.filter(project_id=project.id).aggregate(Sum('amount'))
                single_project = {"title": project.title, "donations": total_donation, "id": project.id}
                my_projects.append(single_project)
            return render(request, 'project/list_all.html', {"projects": my_projects})
    else:
        form = ProjectCreationForm()
        args = {'form': form}
        return render(request, 'project/CreateProject.html', args)


@login_required(login_url='/users/login')  # redirect when user is not logged in
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


@login_required(login_url='/users/login')  # redirect when user is not logged in
def myprojects(request, uid):
    projects = Project.objects.filter(creator_id=uid)
    my_projects = []
    for project in projects:
        total_donation = Donation.objects.filter(project_id=project.id).aggregate(Sum('amount'))
        single_project = {"title": project.title, "donations": total_donation, "id": project.id}
        my_projects.append(single_project)
    return render(request, 'project/list_all.html', {"projects": my_projects})


def project_details(request, pid):
    item = Project.objects.get(id=pid)
    return render(request, 'project/project_details.html', {"item": item})
