from django.shortcuts import render,redirect
from .models import Services,Photographer,Subject
from .forms import ContactUsForm
from django.contrib import messages

# Create your views here.

def home(request):
    subject = Subject.objects.all
    context={
        'subject': subject,

    }
    return render(request,"root/index.html",context=context)


def about(request):
    subject = Subject.objects.all
    context={
        'subject': subject,

    }
    return render(request,"root/about.html",context=context)

def contact(request):
    if request.method =='GET':
        subject = Subject.objects.all
        context={
            'subject': subject,

        }
        return render(request,"root/contact.html",context=context)
    elif request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'we received your message and call with you as soon')
            return redirect('root:contact')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid data')
            return redirect('root:contact')









def services(request):
    service = Services.objects.filter(status=True)
    photographer  = Photographer.objects.filter(status=True)
    subject = Subject.objects.all
    context ={
        'service': service,
        'photographer':photographer,
        'subject': subject,
    }

    return render(request,"root/services.html",context=context)


def gallery(request):
    subject = Subject.objects.all
    context={
        'subject': subject,

    }
    return render(request,"root/gallery.html",context=context)



def gallery_single(request):
    subject = Subject.objects.all
    context={
        'subject': subject,

    }
    return render(request,"root/gallery-single.html",context=context)