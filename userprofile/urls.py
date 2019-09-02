from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name = 'userprofile'
urlpatterns = [
    path('login', views.login_request, name='login'),
    path('change_password', views.changepw_request, name='change_password'),

]
