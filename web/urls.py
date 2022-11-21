from django.contrib import admin
from django.urls import path
from . import views



app_name='web'
urlpatterns = [
    
     path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('sendpost/',views.sendpost,name='sendpost'),
    path('logout/',views.signout,name='logout'),
    path('like/<id>',views.likepost,name='like')
]
