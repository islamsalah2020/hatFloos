from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
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

def view_profile(request, id=None):
    if id:
        user = CustomUser.objects.get(id=id)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = CustomUserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)
