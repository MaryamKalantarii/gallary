from django.shortcuts import render
from .models import Services,Photographer,Subject
# Create your views here.

def home(request):
    return render(request,"root/index.html")


def about(request):
    return render(request,"root/about.html")

def contact(request):
    return render(request,"root/contact.html")

def services(request):
    service = Services.objects.filter(status=True)
    photographer  = Photographer.objects.filter(status=True)
    subject = Subject.objects.all
    context ={
        'service': service,
        'photographer':photographer,
        'subject': subject,
    }
    return render(request,"root/services.html")


def gallery(request):
    return render(request,"root/gallery.html")



def gallery_single(request):
    return render(request,"root/gallery-single.html")