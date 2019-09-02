
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name = 'blog_v1'
urlpatterns = [
    path('bloglist', views.bloglist, name='bloglist'),
    path('blogdetail/<slug:slug>/', views.blogdetail, name='blogdetail'),
    path('blogcreate/', views.blogcreate, name='blogcreate'),
    path('blogdetail/<slug:slug>/update/', views.blogupdate, name='blogupdate'),
]
