from datetime import date
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from DOCTER.models import *
from PATIENT.models import *
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

# Model For Receptionist
class Receptionist(models.Model):
	name = models.CharField(max_length=40)
	phone = models.CharField(max_length=12,default="",unique=True)
	email = models.CharField(max_length=50,unique=True)
	address = models.CharField(max_length=200)
	username = models.OneToOneField(User,on_delete = models.CASCADE)

# Model For Appointment
class Appointment(models.Model):
	docterid = models.ForeignKey('DOCTER.Docter',on_delete = models.CASCADE)
	patientid = models.ForeignKey('PATIENT.Patient',on_delete = models.CASCADE)
	time = models.CharField(max_length =40)
	date = models.CharField(max_length=40,default="")
	status = models.BooleanField(max_length = 15, default=False)


class Payment(models.Model):
	docterid = models.ForeignKey('DOCTER.Docter',on_delete = models.CASCADE)
	patientid = models.ForeignKey('PATIENT.Patient',on_delete = models.CASCADE)
	time = models.CharField(max_length =40)
	date = models.CharField(max_length=40,default="")
	cunsulting=models.BooleanField(default=False)
	extraMedicine=models.IntegerField(default=0) 
	balance=models.IntegerField(default=0)

	def __str__(self):
		return self.patientid.name
		

	
P_CHOICES =(
    ("Q", "Q"),
    ("3X", "3X"),
    ("6X", "6X"),
    ("6", "6"),
    ("30", "30"),("200", "200"),("1M", "1M"),('10M','10M'),('0/1','0/1'),('0/2','0/2'),('0/3','0/3'),('0/4','0/4'),
	('0/5','0/5'),('0/6','0/6'),('0/7','0/7'),('0/8','0/8'),('0/9','0/9'),('0/10','0/10'),('0/11','0/11'),('0/12','0/12'),
	('0/13','0/13'),('0/14','0/14'),('0/15','0/15')
)

D_CHOICES=( ("7 days", "7 days"), ("15 days", "15 days"), ("1 month", "1 month"), ("2 month", "2 month"), ("3 month", "3 month"), ("4 month", "4 month"), ("6month", "6 month"),)

class prescription(models.Model):
	patientid = models.ForeignKey('PATIENT.Patient',on_delete = models.CASCADE)
	medicine = models.CharField(max_length=200)
	potency = models.CharField(choices=P_CHOICES, max_length=50)
	date=models.DateField()
	durations=models.CharField(choices=D_CHOICES, max_length=50)

# Model For HR
class HR(models.Model):
	name = models.CharField(max_length=40)
	phone = models.CharField(max_length=12,default="",unique=True)
	email = models.CharField(max_length=50,unique=True)
	address = models.CharField(max_length=200)
	username = models.OneToOneField(User,on_delete = models.CASCADE)


CHOICES = (
    ("Hedoc", "Hedoc"),
    ("Stomach", "Stomach"),
    ("Brain", "Brain"),
    ("Heart", "Heart"),
    ("Liver", "Liver"),
    ("Kideney", "Kideney"),
    ("Oncho", "Oncho"),
    ("Yash", "Yash"),
)

class Article(models.Model):
    title = models.CharField(max_length=255,choices=CHOICES)
    content = RichTextField(blank=True, null=True)
    content_upload = RichTextUploadingField(blank=True, null=True)






	