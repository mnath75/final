from django import forms
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from .models import *

class QuoteForm(forms.Form):
    test = forms.CharField(max_length=200,
		widget=forms.TextInput(
			attrs={'class' : 'form-control',  'placeholder' : 'Enter Name of Disease', 'aria-lable' : 'Dieases', 'aria-describedly' : 'add-btn'}))

    cause = forms.CharField(max_length= 400,
             widget=forms.TextInput(
			attrs={'class' : 'form-control',  'placeholder' : 'Enter Discription ', 'aria-lable' : 'Discription ', 'aria-describedly' : 'add-btn'}))

###
#class signForm(forms.Form):
  # text = forms.CharField(max_length=200,
	#	widget=forms.TextInput(
		#	attrs={'class' : 'form-control',  'placeholder' : 'question ', 'aria-lable' : 'Dieases', 'aria-describedly' : 'add-btn'}))
  # signature= JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#CCC'}))
###
class SignatureForm(forms.ModelForm):
  signature = JSignatureField()
  class Meta:
    model = JSignatureModel
    fields = ['name','signature']
    exclude = []
    widget = {'height':10}


class ContentsForm(forms.ModelForm):
  class Meta :
    model = Contents
    fields = ['name']
class ItemForm(forms.ModelForm):
  class Meta :
    model = Item 
    fields = ['name','head1','head2']



class Gnm_SbsForm(forms.Form):
    organs = forms.CharField(max_length=200,
		widget=forms.TextInput(
			attrs={'class' : 'form-control',  'placeholder' : 'Enter Name of Organ', 'aria-lable' : 'Organ', 'aria-describedly' : 'add-btn'}))

    conflicts = forms.CharField(max_length= 500,
             widget=forms.TextInput(
			attrs={'class' : 'form-control',  'placeholder' : 'Enter Biological Conflicts ', 'aria-lable' : 'Conflicts ', 'aria-describedly' : 'add-btn'}))
    
