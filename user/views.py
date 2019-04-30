from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.decorators import login_required
from project.models import *
import random


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        print(request.user)

        if form.is_valid():
            form.save()
            # return redirect(reverse('view_profile'))
            # return render(request, 'accounts/profile.html', {'form': form.data})
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    args = {'form': form}
    return render(request, 'accounts/reg_form.html', args)


@login_required(login_url='/users/login')  # redirect when user is not logged in
def view_profile(request, id=None):
    if id:
        user = CustomUser.objects.get(id=id)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)


@login_required(login_url='/users/login')  # redirect when user is not logged in
def edit_profile(request, id=None):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user,
                                    initial={'username': request.user.username, 'first_name': request.user.first_name,
                                             'last_name': request.user.last_name,
                                             'email': request.user.email,
                                             'password': request.user.password, 'DOB': request.user.DOB,
                                             'country': request.user.country,

                                             'phone': request.user.phone, 'FB': request.user.FB,
                                             'picture': request.user.picture})

        args = {'form': form}
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('view_profile', request.user.id)
        else:
            return render(request, 'accounts/edit_profile.html', args)

    else:
        form = CustomUserChangeForm(
            initial={'username': request.user.username, 'first_name': request.user.first_name,
                     'last_name': request.user.last_name,
                     'email': request.user.email,

                     'password': request.user.password, 'DOB': request.user.DOB, 'country': request.user.country,
                     'phone': request.user.phone, 'FB': request.user.FB, 'picture': request.user.picture})

        # form = CustomUserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


@login_required(login_url='/users/login')  # redirect when user is not logged in
def delete_account(request, id=None):
    user = request.user
    user.username = request.user.username + "pbkdf2" + str(random.randint(0, 100))
    user.email = request.user.email + "pbkdf2" + str(random.randint(0, 100))
    user.is_active = False
    user.save()
    return redirect('login')


def top_rated(request):
    top_rated = Rate.objects.all().order_by('-rate')[:5]
    rated_id = []
    rated_pic = []
    print(top_rated)
    for rate in top_rated:
        rated_id.append(rate.project.pk)
    for id in rated_id:
        rated_pic.append(Pic.objects.filter(project_id=id).values('pic').distinct())

    print(rated_pic)
    return HttpResponse(rated_id)


def featured_projects(request):
    featured_projects = FeaturedProject.objects.all().order_by('feature_date')[:5]
    return HttpResponse(featured_projects)


def latest_projects(request):
    latest_projects = Project.objects.all().order_by('start_date')[:5]
    return HttpResponse(latest_projects)

# def search(keyword):
