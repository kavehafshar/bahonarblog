from django.db import models
from django.contrib.auth.models import User


    
class Post(models.Model):
    Name = models.CharField(max_length=20)
    text = models.CharField(max_length=2000)
    likes=models.ManyToManyField(User,related_name='bloglike',blank=True)
    date=models.DateTimeField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.Name



class Comment(models.Model):
    content = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_name=models.CharField(max_length=30,default='kaveh')
    post_connected = models.IntegerField()
    def __str__(self):
        return self.author.first_name














