from django.shortcuts import redirect, render, HttpResponse
from .models import Category, CustomUser, Pic, Project, Donation, ProjectReport, Tag
from comment.models import Comment
from comment.forms import AddCommentForm
from django.db.models import Sum
from project.forms import ProjectCreationForm, CatCreationForm, TagForm, PictureCreationForm
from user.forms import ReportForm
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory


@login_required(login_url='/users/login')  # redirect when user is not logged in
def create(request, uid):
    ImageFormSet = modelformset_factory(Pic, form=PictureCreationForm, extra=4)  # new

    if request.method == 'POST':

        form = ProjectCreationForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Pic.objects.none())  # new

        if form.is_valid() and formset.is_valid:  # new

            project_form = form.save(commit=False)
            project_form.creator = CustomUser.objects.get(id=uid)
            project_form.save()
            # # new
            for form2 in formset.cleaned_data:
                if form2:
                    image = form2['pic']
                    photo = Pic(project=project_form, pic=image)
                    photo.save()
            # end new

            # new 2
            # edit3 = formset.save(commit=False)
            # edit3.project = edit2
            # edit3.save()
            # end new 2
            # list my projects after create new one
            projects = Project.objects.filter(creator_id=uid)
            my_projects = []
            for project in projects:
                total_donation = Donation.objects.filter(project_id=project.id).aggregate(Sum('amount'))
                single_project = {"title": project.title, "donations": total_donation, "id": project.id}
                my_projects.append(single_project)
            return render(request, 'project/list_all.html', {"projects": my_projects})

    else:

        project_form = ProjectCreationForm()
        # pic_form = PictureCreationForm()

        pic_form = ImageFormSet(queryset=Pic.objects.none())  # new
        args = {'project_form': project_form, 'pic_form': pic_form}  # new

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
    # here hard coded for current user till add it from url
    user = CustomUser.objects.get(id=item.creator_id)

    # send pics of project
    images = item.pic_set.all()
    # end
    comments = item.comment_set.all()
    # comments = Comment.objects.all()
    if request.method == "POST":
        commentform = AddCommentForm(request.POST)
        edit = commentform.save(commit=False)
        edit.project = item
        edit.commenter = user

        edit.save()
        form = AddCommentForm()
        return render(request, 'project/project_details.html',
                      {"item": item, "form": form, "comments": comments, "images": images})
    else:
        form = AddCommentForm
        return render(request, 'project/project_details.html',
                      {"item": item, "form": form, "comments": comments, "images": images})


def delete_project(request, pid):
    project = Project.objects.get(id=pid)
    total_donation = Donation.objects.filter(project_id=pid).aggregate(Sum('amount'))
    if total_donation['amount__sum'] is None or total_donation['amount__sum'] < (project.target * 25) / 100:
        project.delete()
    return myprojects(request, request.user.id)


def report_project(request, pid):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        report = ProjectReport()
        if form.is_valid():
            project = Project.objects.get(id=pid)
            report.project = project
            report.msg = request.POST['report_reason']
            report.reporter = request.user
            report.save()
            return myprojects(request, request.user.id)
    else:
        form = ReportForm(request.POST)
        args = {'form': form}
        return render(request, 'project/report_project.html', args)


def tag_project(request, pid):
    if request.method == 'POST':
        form = TagForm(request.POST)
        tag = Tag()
        if form.is_valid():
            project = Project.objects.get(id=pid)
            # tag.project = project.id
            tag.tag = request.POST['tag']
            tag.save()
            return myprojects(request, request.user.id)
    else:
        form = TagForm(request.POST)
        args = {'form': form}
        return render(request, 'project/tag_project.html', args)
