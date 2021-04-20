from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from .models import Contact


# Create your views here.
def index(request):
    if request.method=="POST":
        usn=request.POST.get('usn', '')
        name=request.POST.get('name', '')
        sem=request.POST.get('sem', '')
        phone=request.POST.get('phone', '')
        email=request.POST.get('email', '')
        if usn and name and sem and phone and email:
             contact=Contact(usn=usn,name=name,sem=sem,phone=phone)
             contact.save()
        else:
            return HttpResponse("enter all the details")
    return render(request, 'index.html')