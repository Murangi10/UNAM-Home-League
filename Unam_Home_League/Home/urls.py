
from django.urls import path
from . import views 

urlpatterns = [
    
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('gallery/', views.gallery, name="gallery"),
    path('bima/', views.bima, name="bima"),
    #path('braves/', views.braves, name="braves"),
    path('chipolopolo/', views.chipolopolo, name="chipolopolo"),
    path('flyzone/', views.flyzone, name="flyzone"),
    path('rangers/', views.rangers, name="rangers"),
    #path('inter/', views.inter, name="inter"),
    path('table/', views.display_Log, name="table"), 
    path('military/', views.military, name="military"),
    path('fixtures/', views.display_Fixtures, name="fixtures"),
    path('contact/', views.contact, name="contact"),
    path('results/', views.display_Results, name="results"),
    
]
