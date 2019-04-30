from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.decorators import login_required
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from project.models import *
import random
from django.core.mail import EmailMessage


# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST, request.FILES)
#         print(request.user)
#
#         if form.is_valid():
#             form.save()
#             # return redirect(reverse('view_profile'))
#             # return render(request, 'accounts/profile.html', {'form': form.data})
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm()
#
#     args = {'form': form}
#     return render(request, 'accounts/reg_form.html', args)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Activation link is true')
        # return HttpResponse("Thank you for your email confirmation. Now you can go to your homepage")
    else:
        return HttpResponse('Activation link is invalid!')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        # profile_form=UserProfileForm(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # profile = profile_form.save(commit=False)
            # profile.user = user
            # profile.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Hatfloos account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            user.is_active = False
            user.save()
            return render(request, 'check_mail.html')
    else:
        form = CustomUserCreationForm()
        # profile_form = UserProfileForm()
    return render(request, 'accounts/reg_form.html', {
        'form': form,
        # 'profile_form': profile_form
    })


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


def search(request):
    projects = Project.objects.filter(title=request.GET.q).get('title') or Tag.object.filter(tag=request.GET.q).get(
        'title')
    return HttpResponse(projects)
