from django.urls import path
from . import views

urlpatterns = [

    path('create', views.create, name='create'),
    path('create_cat', views.create_cat, name='create'),
    path('<int:uid>/projects', views.myprojects, name='create'),

    # path('<int:id>', views.view_profile, name='view_profile'),
    # # path(r'^profile/(?P<id>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    # # # path('edit/<int:id>', views.edit_profile, name='edit_profile'),
    # path(r'<int:id>/edit/', views.edit_profile, name='edit_profile'),
]
