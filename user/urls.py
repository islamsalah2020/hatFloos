from django.urls import path
from . import views

urlpatterns = [
    # path('<int:id>', views.get_user_info),
    path('register', views.register, name='register'),
    path('<int:id>', views.view_profile, name='view_profile'),
    # path(r'^profile/(?P<id>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    path('edit/<int:id>', views.edit_profile, name='edit_profile'),
    path('<int:id>/delete', views.delete_account),
    # path(r'<int:id>/edit/', views.edit_profile, name='edit_profile'),
]
