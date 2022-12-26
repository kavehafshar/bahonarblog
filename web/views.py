from django.shortcuts import render , redirect ,reverse
from web.models import Post,Comment
from django.http import HttpResponse ,HttpRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt 
from django.db import models
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import login,logout
from .forms import *
from django import forms
from django.contrib.auth.models import User
import datetime


# Create your views here.
def signup(request):
    if request.method=='POST':
        form=signupForm(request.POST)
        if form.is_valid():
            firstname=form.cleaned_data['name'] 
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=User.objects.create_user(username, password=password)
            user.first_name=firstname
            user.save()
            login(request, user)
            return redirect('/')
    return render(request,'webview/signup.html')



def signin(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect('/')
    return render(request, 'webview/signin.html')



def signout(request):
    if request.method=='POST':
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
    if request.method == 'POST':
        form=SendPostForm(request.POST)
        if form.is_valid():
            Name=form.cleaned_data['Name']
            text=form.cleaned_data['text']
            date=datetime.datetime.now()
            user=request.user           
            newpost=Post.objects.create(Name=Name,text=text,date=date,user=user)
            newpost.save()
            return redirect('/')
    return render(request, 'webview/sendpost.html')
    
    

def likepost(request,id):
    posti=Post.objects.get(id=id)
    user=request.user
    posti.likes.add(user)
    return redirect(reverse('likepost'))
    return redirect(request.META['HTTP_REFERER'])




def yourposts(request):
    posts=Post.objects.all()
    ordered=posts.order_by('id')
    context={'posts':ordered}
    return render(request, 'webview/yourposts.html',context)
    


def comment(request,id):
    comments=Comment.objects.filter(post_connected=id).values()
    context={'Comments':comments}
    return render(request,'webview/comment.html',context)



def sendComment(request,id):
     if request.method=='POST':
        form=SendCommentForm(request.POST)
        if form.is_valid():
            content=form.cleaned_data['content']
            author=request.user
            author_name=request.user.first_name
            new_comment = Comment.objects.create(content=content, author=author, post_connected=id,author_name=author_name)
            new_comment.save()
            return comment(request,id)