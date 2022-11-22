from re import template
from django.shortcuts import render , redirect

from . models import *
# Create your views here.

def index(request):
    return render(request,'index.html')


def chiefcomplaints(request):
    return render(request,'dashboard/templates/all-customer.html')

def fearIncidents(request):
    return render(request,'dashboard/templates/fear_&_incidents.html')

def pasthistory(request):
    return render(request,'dashboard/templates/past-history-of-illness.html')

def familymedical(request):
    return render(request,'dashboard/templates/familymedical.html')


def personalhabits(request):
    return render(request,'dashboard/templates/personal-habits.html')


def personalappetite(request):
    return render(request , "dashboard/templates/appetite.html")


def infood(request):
    return render(request,'dashboard/templates/infood.html')

def sexualsphere(request):
    return render(request,'dashboard/templates/sexual-sphere.html')

def investigation(request):
    return render(request,'dashboard/templates/investigation.html')

def thermalreaction(request):
    return render(request,'dashboard/templates/thermal.html')

def rubricselection(request):
    return render(request,'dashboard/templates/Rubric-selection.html')

def allstaff(request):
    return render(request,'dashboard/templates/all-staff.html')

def editstaff(request):
    return render(request,'dashboard/templates/edit-staff.html')


def addstaff(request):
    return render(request,'dashboard/templates/add-staff.html')

def gallery(request):
    return render(request,'dashboard/templates/gallery.html')


def allroom(request):
    return render(request,'dashboard/templates/all-rooms.html')

def addroom(request):
    return render(request,'dashboard/templates/add-room.html')

def editroom(request):
    return render(request,'dashboard/templates/edit-room.html')

def pagination(request):
    return render(request,'dashboard/templates/responsivepage.html')

def drum1bottle(request):
    return render(request,'dashboard/templates/drum_1_bottle.html')

def halfdrumbottle(request):
    return render(request,'dashboard/templates/half_drum_bottle.html')

def pills(request):
    return render(request,'dashboard/templates/pills.html')


def demo(request):
    return render(request,'dashboard/templates/deno.html')

def mental(request):
    return render(request,'dashboard/templates/mind_causative_factor.html')



def multiple(request):
    return render(request,'dashboard/templates/multiple.html')

def miasm(request):
    return render(request,'dashboard/templates/miasm.html')


def multipleselect(request):
    return render(request,'multipleselect.html')

def personalappetite(request):
    return render(request,'dashboard/templates/appetite.html')

def lifestory(request):
    return render(request,'dashboard/templates/life_story.html')


def accordian(request):
    return render(request,'dashboard/templates/accordian.html')

def addmedicine(request):
    return render(request,'dashboard/templates/add-room.html')


def addstaff(request):
    return render(request,'dashboard/templates/add-staff.html')

def book(request):
    return render(request,'dashboard/templates/book.html')

def item(request):
    return render(request,'dashboard/templates/item.html')

def itemDetail(request):
    return render(request,'dashboard/templates/itemDetail.html')

def one_drum_bottles(request):
    return render(request,'dashboard/templates/drum_1_bottle.html')

def half_drum_bottle(request):
    return render(request,'dashboard/templates/half_drum_bottle.html')

def pills(request):
    return render(request,'dashboard/templates/pills.html')





def upload_images(request):
	return render(request,'upload.html')



def add_question(request):
    if request.method=='POST':
        questions=request.POST['questions']
        obj=Question.objects.create(question=questions)
        obj.save()
    return render(request,'dashboard/templates/add_question.html')


def retrive(request):
    status=False
    if request.user:
        status=request.user
    obj=Question.objects.all()
    print(obj)
    return render(request,'all-customer.html', {'obj':obj} )


