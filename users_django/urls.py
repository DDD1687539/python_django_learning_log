# Coder: Lee
# Time:  2022/11/13 22:46

from django.urls import re_path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users_django'

urlpatterns = [
    re_path(r'^login/$', LoginView.as_view(template_name='users_django/login.html'), name='login'),
    re_path(r'^logout/$', views.logout_view, name='logout'),
    re_path(r'^register/$', views.register, name='register'),
]



