from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    question=models.TextField()
    username = models.OneToOneField(User,on_delete = models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.username
    