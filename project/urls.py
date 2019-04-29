from django.urls import path
from . import views

urlpatterns = [

    path('create_cat', views.create_cat, name='create'),
    path('x/<int:pid>', views.project_details, name='create'),
    path('<int:uid>/projects', views.myprojects, name='create'),
<<<<<<< HEAD
]
=======
    path('<int:uid>/donations', views.myprojects, name='create'),
    path('<int:uid>/create', views.create, name='create'),
]
>>>>>>> a219f84c6d3762df736f7785df8ebca2dd5c15e8
