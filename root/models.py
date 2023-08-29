from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name




class Subject(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name




class Skills(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name




class Photographer(models.Model):
    info = models.ForeignKey(User , on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    description = models.TextField()
    image = models.ImageField(upload_to='photographer', default='photographer.jpg')
    status = models.BooleanField(default=False)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.info.username
    


class Services(models.Model):
    client =  models.ManyToManyField(Client)
    subject= models.ManyToManyField(Subject)
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField(default=0)
    photographer = models.ForeignKey(Photographer,on_delete=models.CASCADE)
    available_seat = models.IntegerField(default=0)
    schedule = models.DateTimeField(default=datetime.datetime.now())
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    
    def capt(self):
        return self.title.capitalize()



class ContactUs (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return self.name