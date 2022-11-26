from django import forms

class SendPostForm(forms.Form):
    Name=forms.CharField(label='Name', max_length=20)
    text=forms.CharField(label='text', max_length=2000)

class signupForm(forms.Form):
    name=forms.CharField(label='name',max_length=20)
    username=forms.CharField(label='username',max_length=20)
    password=forms.CharField(label='password',max_length=20)