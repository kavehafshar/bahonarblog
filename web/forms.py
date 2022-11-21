from django import forms

class SendPostForm(forms.Form):
    Name=forms.CharField(label='your Name', max_length=20)
    text=forms.CharField(label='your text', max_length=2000)