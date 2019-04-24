

from django.urls import path
from . import views

urlpatterns = [
    # path('<int:id>', views.get_user_info),
    path('<int:id>', views.view_profile, name='view_profile'),
    path(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),

]