from django.shortcuts import render
from .models import *

from Home.forms import ContactForm  

# Create your views here.

def index(request):
    return render(request, 'Home/index.html')
def about(request):
    return render(request, 'Home/about.html')
def gallery(request):
    return render(request, 'Home/gallery.html')
def bima(request):
    return render(request, 'Home/bima.html')
def chipolopolo(request):
    return render(request, 'Home/chipolopolo.html')
def rangers(request):
    return render(request, 'Home/rangers.html')
def flyzone(request):
    return render(request, 'Home/flyzone.html')
def table(request):
    return render(request, 'Home/table.html')
def military(request):
    return render(request, 'Home/military.html')
def fixtures(request):
    return render(request, 'Home/fixtures.html')   
def contact(request):
    return render(request, 'Home/contact.html')
def results(request):
    return render(request, 'Home/results.html')

def display_Log(request):
    items = Log_Standing.objects.all()
    context = {
        'items': items,
        
    }
    return render(request, 'Home/table.html', context)
    
def display_Fixtures(request):
    teams = Fixtures.objects.all()
    context = {
        'teams': teams,
        
    }
    return render(request, 'Home/fixtures.html', context)  

def display_Results(request):
    results = Results.objects.all()
    context = {
        'results': results,
        
    }
    return render(request, 'Home/results.html', context)

def contact(request):  
    stu = ContactForm(request.POST)
    if stu.is_valid():
        stu.save() 
    return render(request,"Home/contact.html",{'form':stu}) 