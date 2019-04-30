from django.urls import path
from . import views

urlpatterns = [

    path('create_cat', views.create_cat, name='create'),
    path('x/<int:pid>', views.project_details, name='create'),
    path('<int:uid>/projects', views.myprojects, name='create'),
    path('<int:uid>/donations', views.myprojects, name='create'),
    path('<int:uid>/create', views.create, name='create'),
    path('<int:pid>/delete', views.delete_project, name='delete_project'),
    path('<int:pid>/report', views.report_project, name='report_project'),
    path('<int:pid>/tag', views.tag_project, name='tag_project'),
]

