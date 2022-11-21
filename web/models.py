from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Token(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    token=models.CharField(max_length=12)
    def __str__(self):
        return self.user
    
class Post(models.Model):
    Name = models.CharField(max_length=20)
    text = models.CharField(max_length=2000)
    likes=models.ManyToManyField(User,related_name='bloglike',blank=True)
    def __str__(self):
        return self.Name
