from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


    
class Post(models.Model):
    Name = models.CharField(max_length=20)
    text = models.CharField(max_length=2000)
    likes=models.ManyToManyField(User,related_name='bloglike',blank=True)
    def __str__(self):
        return self.Name
