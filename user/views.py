from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.decorators import login_required


# def get_user_info(request, id):
#     user = models.CustomUser.objects.get(id=id)
#     if request.method == 'GET':
#         user_form = forms.UserProfileForm(
#             initial={'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email,
#                      'password': user.password, 'date': user.DOB, 'country': user.country, 'phone': user.phone})
#     else:
#         pass
#
#     return render(request, 'user/profile.html', {"form": user_form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
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


def view_profile(request, id=None):
    if id:
        user = CustomUser.objects.get(id=id)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)


def edit_profile(request, id=None):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('view_profile', request.user.id)
    else:
        form = CustomUserChangeForm(
            initial={'username': request.user.username, 'first_name': request.user.first_name,
                     'last_name': request.user.last_name,
                     'email': request.user.email,
                     'password': request.user.password, 'date': request.user.DOB, 'country': request.user.country,
                     'phone': request.user.phone})
        # form = CustomUserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


def delete_account(request,id=None):
    user = request.user
    user.is_active = False
    user.save()
    return redirect('login')
