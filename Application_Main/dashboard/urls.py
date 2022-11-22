from pathlib import Path
from unicodedata import name
from django.urls import path
from .views import demo, index,chiefcomplaints,fearIncidents,accordian,personalappetite,mental,lifestory ,pills,miasm,multipleselect, pasthistory,pagination,familymedical,multiple,personalhabits,halfdrumbottle ,drum1bottle,gallery, pills, sexualsphere,investigation,thermalreaction,rubricselection,allstaff,editstaff,addstaff,allroom,addroom,editroom
urlpatterns = [
    path('index/', index ,name='index'),
    path('chiefcomplaints/', chiefcomplaints ,name='chiefcomplaints'),
    path('fearIncidents/',fearIncidents, name='fearIncidents'),
    path('past/', pasthistory , name='past'),
    path('familymedical/',familymedical, name='familymedical'),
    path('personalhabits/',personalhabits, name='personalhabits'),
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
    

]
