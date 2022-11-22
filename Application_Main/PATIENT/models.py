from django.db import models


# import in-Built User Models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
	name = models.CharField(max_length=40)
	phone = models.CharField(max_length=12,default="",unique=True)
	email = models.CharField(max_length=50,unique=True)
	branch = models.CharField(max_length=200,default='',null=True)
	gender = models.CharField(max_length=30)
	address = models.CharField(max_length=200)
	age = models.IntegerField(default= 0 )
	blood = models.CharField(max_length=10)
	medical = models.CharField(max_length=100)
	case = models.CharField(max_length=20)
	username = models.OneToOneField(User,on_delete = models.CASCADE)

class Invoice(models.Model):
	patient = models.OneToOneField(Patient,on_delete = models.CASCADE)
	outstanding = models.CharField(max_length =  10)
	paid = models.CharField(max_length = 10)



class MultipleUploadImages(models.Model):
	images = models.FileField(upload_to='images', null=True)
	#image = models.ImageField(upload_to='images', null=True)
	image= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
