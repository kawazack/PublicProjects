"""AprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

#Import App with my created views
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('hello-world/', views.hello_world, name = "hello_world"),
    path('test-page/', views.test_page, name = "test_page"),
    path('test-page/<int:redirection>/', views.test_page, name = "test_page"),
    path('contact/', views.contact, name="contact"),
    path('contact/<str:name>/', views.contact, name="contact"),
    path('contact/<str:name>/<str:surname>/', views.contact, name="contact")
]