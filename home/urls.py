from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.registeruser, name='register'),
    path('wordgame/', views.wordgameplay, name='wordgame'),
    path('wordgameresult/', views.wordgameresult, name='wordgameresult'),

]
