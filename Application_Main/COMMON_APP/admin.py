from django.contrib import admin
from .models import Article
# Register your models here.
from .models import *
admin.site.register(Receptionist)
admin.site.register(Appointment)
admin.site.register(HR)
admin.site.register(Article)




