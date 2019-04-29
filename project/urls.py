from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('create_cat', views.create_cat, name='create'),
    path('x/<int:pid>', views.project_details, name='create'),
    path('<int:uid>/projects', views.myprojects, name='create'),
]