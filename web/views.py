from django.shortcuts import render , redirect
from web.models import Post 
from django.http import HttpResponse ,HttpRequest
from django.views.decorators.csrf import csrf_exempt 
from django.db import models
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import login,logout
from .forms import SendPostForm
from django import forms

# Create your views here.


def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('/')


    form=UserCreationForm()
    return render(request, 'webview/signup.html',{'form':form})

def signin(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect('/')

    form=AuthenticationForm()
    return render(request, 'webview/signin.html',{'form':form})

def signout(request):
    if request.method=='POST':
        print('\n\n\n----------------\n\n\nHOI\n\n\n------------\n\n\n')
        logout(request)
        #return redirect('/')
        return redirect('/')

    return render(request, 'webview/logout.html')


def home(request):
    posts=Post.objects.all()
    ordered=posts.order_by('-id')
    context={'posts':ordered}
    return render(request, 'webview/home.html',context)
 
def sendpost(request):
    form=SendPostForm()
    if request.method == 'POST':
        form=SendPostForm(request.POST)
        if form.is_valid():
            Name=form.cleaned_data['Name']
            text=form.cleaned_data['text']
            newpost=Post.objects.create(Name=Name,text=text)
            newpost.save()
            return redirect('/')
    context={'form':form}   
    return render(request, 'webview/sendpost.html',context)
    
