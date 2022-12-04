"""Application_Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from COMMON_APP.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from dashboard.views import *
from DOCTER.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    # Home Page
    path('', home , name = 'home' ),
    path('register', register , name = 'register' ),
    path('login', login , name = 'login' ),
    path('about', about , name = 'about' ),

    path('logout', logout , name = 'logout' ),
    path('profile/(?P<user>.*)', profile , name = 'profile' ),
    path('dashboard/(?P<user>.*)', dashboard , name = 'dashboard'),
    path('receptionist_dashboard/(?P<user>.*)', receptionist_dashboard , name = 'receptionist_dashboard'),

    

    path('create_appointment/(?P<user>.*)', create_appointment , name = 'create_appointment'),
    path('delete_patient/(?P<id>\d+)', delete_patient , name = 'delete_patient'),
    path('update_patient/(?P<id>\d+)', update_patient , name = 'update_patient'),

    path('create_patient/', create_patient , name = 'create_patient'),
    path('myappointment/', myappointment , name = 'myappointment'),
    path('docter_appointment/', docter_appointment , name = 'docter_appointment'),
    path('docter_prescription/', docter_prescription , name = 'docter_prescription'),
    path('create_prescription/', create_prescription , name = 'create_prescription'),
    path('medical_history/', medical_history , name = 'medical_history'),
    path('update_status/(?P<id>\d+)', update_status , name = 'update_status'),
    path('hr_dashboard/', hr_dashboard , name = 'hr_dashboard'),
    path('hr_accounting/', hr_accounting , name = 'hr_accounting'),
    path('update_docter/(?P<id>\d+)', update_docter , name = 'update_docter'),
    path('delete_docter/', delete_docter , name = 'delete_docter'),
    path('patient_invoice/', patient_invoice , name = 'patient_invoice'),
    path('get_pdf/(?P<id>\d+)', get_pdf , name = 'get_pdf'),
    path('send_reminder/(?P<id>\d+)', send_reminder , name = 'send_reminder'),
    path('apointmentDetails/(?P<id>\d+)', apointmentDetails , name = 'apointmentDetails'),
    path('payment/(?P<id>)', payment , name = 'payment'),
    #path('create_prescription/',create_prescription , name = 'create_prescription'),
    path('patientdetail/', patientDetail , name = 'patientDetail'),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('quote/', quotation , name = 'quote'),
    path('organsconflicts/', Gnm_Sbs_Conflicts , name='Gnm_Sbs_Conflicts'),

    path('delete_organs/<int:id>/', delete_organs , name = 'delete_organs'),
    path('delete_quote/<int:id>/',delete_quote, name='delete_quote' ),

    path('mysign',my_sign , name = 'mysign'),
    path('index/',index,name='dashboard'),
    path('chiefcomplaints/', chiefcomplaints ,name='chiefcomplaints'),
    path('fearIncidents/',fearIncidents, name='fearIncidents'),
    path('past/', pasthistory , name='past'),
    path('familymedical/',familymedical, name='familymedical'),
    path('personalhabits/',personalhabits, name='personalhabits'),
    path('personalappetite/', personalappetite , name='personalappetite'),
    path('infood/', infood , name='infood'),
    path('sexualsphere/',sexualsphere, name='sexualsphere'),
    path('investigation/',investigation,name='investigation'),
    path('thermalreaction/',thermalreaction,name="thermalreaction"),
    path('rubricselection/', rubricselection, name="rubricselection"),
    path('allstaff/',allstaff, name="allstaff"),
    path('addstaff/',addstaff, name="addstaff"),
    path('editstaff/',editstaff, name="editstaff"),
    path('gallery/',gallery,name="gallery"),
    path('allrooms/',allroom,name="allroom"),
    path('addrooms/',addroom,name="addroom"),
    path('editrooms/',editroom,name="editroom"),
    path('pagination/',pagination,name="pagination"),
    path('drum1bottle/',drum1bottle,name="drum1bottle"),
    path('halfdrumbottle/',halfdrumbottle,name="halfdrumbottle"),
    path('pills/',pills,name="pills"),
    path('multiple/',multiple,name="multiple"),
    path('mind2/',demo,name="mind2"),
    path('mental/',mental,name="mental"),
    path('miasm/',miasm,name='miasm'),
    path('multipleselect/',multipleselect,name="multipleselect"),
    path('personalappetite/',personalappetite,name='personalappetite'),
    path('lifestory/',lifestory,name='lifestory'),
    path('accordian/',accordian,name='accordian'),
    path('appointment/',appontment, name='appontment'),
    path('ordermedi1cine/',ordermedi1cine, name='ordermedi1cine'),
    path('addmedicine/',addmedicine, name='addmedicine'),
    path('addstaff/',addstaff, name='addstaff'),
    path('one_drum_bottles/', one_drum_bottles, name='one_drum_bottles'),
    path('half_drum_bottle/', half_drum_bottle , name='half_drum_bottle'),
    path('pills/', pills , name='pills' ),
    


    #path('create', views.ExampleCreateView.as_view(), name='create'),
    path('book/',book,name='book'),
    path('list/',list,name='list'),
    path('listdetails/<int:pk>/',listdetails,name='listdetails'),
    
    path('upload_images/',upload_images, name='upload_images'),


    
    path('myitem/<int:pk>/', myitem, name='myitem'),
    path('delitem/<int:pk>/', delitem, name='delitem'),
    path('deless/<int:id>/<int:pk>/', deless, name='deless'),
    path('delh1/<int:id>/<int:pk>/', delh1, name='delh1'),
    path('delh2/<int:id>/<int:pk>/', delh2, name='delh2'),
    path('delan/<int:id>/<int:pk>/', delan, name='delan'),
    
    path('delitem2/<int:id>/<int:pk>/', delitem2, name='delitem2'),

    path('itemDetail/<int:pk>/', itemDetail, name='itemDetail'),
    path('ess/<int:pk>/', ess, name='ess'),
    path('he1/<int:pk>/', he1, name='he1'),
    path('he2/<int:pk>/', he2, name='he2'),
    path('ana/<int:pk>/', ana, name='ana'),
    path('dash_patients_details/(?P<user>.*)',dash_patients_details, name="patients_details"),
    path('dash_appointment_details/(?P<user>.*)', dash_appointment_details, name="appointment_details"),
    path('repeat_med_details/(?P<user>.*)',repeat_med_details, name="repeat_medicicne"),
    path('courier_medicine/(?P<user>.*)',courier_medicine, name="courier_medicicne"),
    path('online_consultation/(?P<user>.*)',online_consultation, name="online_consultation"),
    path('add_question/',add_question, name='add_question'),
    path('retrive/',retrive, name='retrive'),
    


]
urlpatterns += static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)


