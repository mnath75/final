from unittest.util import _MAX_LENGTH
from django.db import models
from PATIENT.models import *
from .models import *
from COMMON_APP.models import *
# Create your models here.
from jsignature.fields import JSignatureField
from django.contrib.auth.models import User
from jsignature.mixins import JSignatureFieldsMixin

# Create your models here.
class Docter(models.Model):
	name = models.CharField(max_length=40)
	phone = models.CharField(max_length=12,default="",unique=True)
	email = models.CharField(max_length=50,unique=True)
	gender = models.CharField(max_length=30)
	address = models.CharField(max_length=200)
	age = models.IntegerField(default= 0)
	blood = models.CharField(max_length=10)
	username = models.OneToOneField(User,on_delete = models.CASCADE)
	status = models.BooleanField(default = 0)
	department = models.CharField(max_length=30 , default = "")
	attendance = models.IntegerField(default = 0)
	salary = models.IntegerField(default = 10000)
	


	
# Prescription Model


class Prescription2(models.Model):
	prescription = models.CharField(max_length=200)
	symptoms = models.CharField(max_length=200)
	patient = models.ForeignKey(Patient,on_delete = models.CASCADE,unique = False)
	docter = models.ForeignKey(Docter,on_delete = models.CASCADE,unique = False)
	appointment = models.ForeignKey('COMMON_APP.Appointment',on_delete = models.CASCADE,unique = False)
	prescripted_date = models.DateField(auto_now = True) 
	outstanding = models.IntegerField(default = 0)
	paid = models.IntegerField(default = 0)
	total = models.IntegerField(default = 0)


# HR Dashboard Data


class Quote(models.Model):
	test = models.CharField(max_length=200)
	cause = models.CharField(max_length=400)

	def __str__(self):
		return( self.test)
class sign(models.Model):
	text = models.CharField(max_length=200,null=True , blank=True)
	signature = JSignatureField(null=True, blank=True)
class JSignatureModel(JSignatureFieldsMixin):
    name = models.CharField(max_length=20)
    signature = JSignatureField()



class Contents(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return( self.name )
class Item(models.Model):
	content = models.ForeignKey(Contents, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	head1= models.CharField(max_length=200)
	head2 = models.CharField(max_length=200)
	def __str__(self):
		return( self.name)
class Essence(models.Model):
	name = models.CharField(max_length=200)
	item = models.ForeignKey(Item, on_delete=models.CASCADE,related_name ='essence_itom')
	def __str__(self):
		return(self.name)
class Head1(models.Model):
	name = models.CharField(max_length=200)
	item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'head1_item')
	def __str__(self):
		return(self.name)
class Head2(models.Model):
	name = models.CharField(max_length=200)
	item = models.ForeignKey(Item, on_delete=models.CASCADE,related_name ='head2_item')

	def __str__(self):
		return(self.name)

class Medicine(models.Model):
	name = models.CharField(max_length=200)
	item = models.ForeignKey(Item, on_delete=models.CASCADE,related_name ='medicine_item')
	def __str__(self):
		return(self.name)	
class Analysis(models.Model):
	name = models.CharField(max_length=200)
	item = models.ForeignKey(Item, on_delete=models.CASCADE,related_name ='analysis_item')
	def __str__(self):
		return(self.name)	



class Gnm_Sbs(models.Model):
	Organs = models.CharField(max_length=200)
	Conflicts = models.CharField(max_length=400)

	def __str__(self):
		return( self.organs)





