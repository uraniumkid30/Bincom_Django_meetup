from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .forms import *
from django.core.mail import send_mail
from site_utils import WordGame

from django import template
register = template.Library()
@register.filter('get_value_from_dict')
def get_value_from_dict(dict_data,key):
    if key:
        return  dict_data.get(key)
def mailsender(var):
    subject = 'greetings from bobby'
    message = 'this is just a cool message '
    emailFrom = 'uraniumkid30@gmail.com'
    emailTo = [var,]
    try:
        send_mail(subject,message,emailFrom,emailTo,fail_silently=True)
    except Exception as e:
        print(e)
def homepage(request):
    d=timezone.now().second
    if d%2 ==0 :
        c='even'
    else:
        c='odd'
    context={'time':{1:[10,20,30],2:[100,200,300]}}
    messages.success(request,'hello!!!, you are welcome to our site')
    return render(request,'home/home.html',context=context)

def registeruser(request):
    if request.method == 'POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            print('okay na')
            mailsender(form.cleaned_data['email'])
        else:
            print('wahala')
            #user=form.save()
            #login(request,user)
        context = {'form': form}
    else:
        form = NewUserForm()
        context = {'form':form}

    return render(request,'home/register.html',context=context)

def wordgameplay(request):
    form = WordForm()
    context = {'form': form}

    return render(request,'home/letterpuzzle.html',context=context)

def wordgameresult(request):
    if request.method == 'POST':
        form= WordForm(request.POST)
        if form.is_valid():
            letters = form.cleaned_data['letters']
            words = WordGame(letters)
            words.allwords()
            words.actualwords()
            context = {'words': words.bank2}
            print(form.cleaned_data['letters'])
            return render(request,'home/wordsolution.html',context=context)
    else:
        form = WordForm()
        context = {'form': form}

        return render(request, 'home/letterpuzzle.html', context=context)