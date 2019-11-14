"""Unam_Home_League URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('Home.urls')),
    path('about/', include('Home.urls')),
    path('gallery/', include('Home.urls')),
    path('bima/', include('Home.urls')),
    path('chipolopolo/', include('Home.urls')),
    path('flyzone/', include('Home.urls')),
    path('rangers/', include('Home.urls')),
    path('table/', include('Home.urls')),
    path('military/', include('Home.urls')),
    path('fixtures/', include('Home.urls')),
    path('contact/', include('Home.urls')),
    path('results/', include('Home.urls')),
     
]
