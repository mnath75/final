from email.utils import quote
from xml.dom.minidom import NamedNodeMap
from django.shortcuts import render , redirect , HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import View
from django import template
from django.urls import reverse
from django.template.loader import get_template
from io import BytesIO
import xhtml2pdf.pisa as pisa
from .models import * 
from .forms import *

# Create your views here.

def book(request):
    if request.method =='POST' :
        form = ContentsForm(request.POST)
        if form.is_valid():
            new_todo = Contents(name=request.POST['name'])
            new_todo.save()
            return redirect('book')
    form = ContentsForm(request.POST)
    books = Contents.objects.all()
    contest = { 'books':books,'form':form}
    return render(request,'Dashboard/templates/book.html',contest)
def delitem(request,pk):
    cont=Contents.objects.get(pk=pk)
    
    cont.delete()
    return redirect ('book')
def delitem2(request,id,pk):
    cont=Item.objects.get(pk=id)
    cont.delete()  

    return redirect (reverse(myitem , kwargs = {'pk': pk }))
def deless(request,id,pk):
    cont=Essence.objects.get(pk=id)
    cont.delete() 
    return redirect (reverse(itemDetail , kwargs = {'pk': pk })) 

    
def delh1(request,id,pk):
    cont=Head1.objects.get(pk=id)
    cont.delete() 
    return redirect (reverse(itemDetail , kwargs = {'pk': pk })) 
 

def delh2(request,id,pk):
    cont=Head2.objects.get(pk=id)
    cont.delete()

    return redirect (reverse(itemDetail , kwargs = {'pk': pk }))
def delan(request,id,pk):
    cont=Analysis.objects.get(pk=id)
    cont.delete() 
    return redirect (reverse(itemDetail , kwargs = {'pk': pk }))


def myitem(request,pk):
    cont=Contents.objects.get(pk=pk)
    if request.method == 'POST':
     #   form = ItemForm(request.POST)
        #if form.is_valid():                   
            new_todo = Item(content=cont , name = request.POST['name'],head1=request.POST['head1'],head2=request.POST['head2'])
            new_todo.save()
            return redirect (reverse(myitem , kwargs = {'pk': pk }))        
    item = Item.objects.filter(content=cont)
     # essence=Essence.objects.filter(item=item.id)
    #head1=Head1.objects.filter(item=item.id)
    #head2=Head2.objects.filter(item=item.id)
    #analysis=Analysis.objects.filter(item=item.id)
    #form = ItemForm(request.POST)
    contest={'item' : item, 'pk' : pk }
    return render (request,'Dashboard/templates/item.html',contest)



def itemDetail(request,pk):
    it=Item.objects.get(pk=pk)
    if request.method == 'POST':
        return redirect (reverse(myitem , kwargs = {'pk': pk })) 
    essence=Essence.objects.filter(item=it)
    head1=Head1.objects.filter(item=it)
    head2=Head2.objects.filter(item=it)
    analysis=Analysis.objects.filter(item=it)
    content={'it':it,'head1':head1,'head2':head2,'analysis':analysis,'essence':essence,'id':pk}
    return render(request,'Dashboard/templates/itemDetail.html',content)
def ess(request,pk):
    name1=request.GET.get('name1')
    name2=request.GET.get('name2')
    name3=request.GET.get('name3')
    name4=request.GET.get('name4')
    it=Item.objects.get(pk=pk)
    if name1 :
        obj=Essence(item=it,name=name1)
        obj.save()
    if name2 :        
        obj=Head1(item=it,name=name2)
        obj.save()
    if name3 :        
        obj=Head2(item=it,name=name3)
        obj.save()
    if name4 :
        obj=Analysis(item=it,name=name4)
        obj.save()
    return redirect (reverse(itemDetail , kwargs = {'pk': pk }))
    
    


def he1(request,pk):
    
    print(name)
    
    return redirect (reverse(itemDetail , kwargs = {'pk': pk }))
def he2(request,pk):
    name=request.GET.get('name3')
    print(name)
    
    return redirect (reverse(itemDetail , kwargs = {'pk': pk }))
def ana(request,pk):
    name=request.GET.get('name4')
    print(name)
    it=Item.objects.get(pk=pk)
    obj=Analysis(item=it,name=name)
    obj.save()
    return redirect (reverse(itemDetail , kwargs = {'pk': pk }))
def list(request):
    ls=Item.objects.all().order_by()
    contest = {'ls':ls}
    return render(request,'Dashboard/templates/list.html',contest)
def listdetails(request,pk):
    it=Item.objects.get(pk=pk) 

    essence=Essence.objects.filter(item=it)
    head1=Head1.objects.filter(item=it)
    head2=Head2.objects.filter(item=it)
    analysis=Analysis.objects.filter(item=it)
    content={'it':it,'head1':head1,'head2':head2,'analysis':analysis,'essence':essence,'id':pk}
    return render(request,'Dashboard/templates/itemDetail.html',content)






    

