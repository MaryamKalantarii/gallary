from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name




class Photographer(models.Model):
    info = models.ForeignKey(User , on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    description = models.TextField()
    image = models.ImageField(upload_to='photographer', default='photographer.png')
    # twitter = models.CharField(max_length=255, default='#')
    # facebook = models.CharField(max_length=255, default='#')
    # instagram = models.CharField(max_length=255, default='#')
    # linkdin = models.CharField(max_length=255, default='#')
    status = models.BooleanField(default=False)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.info.username
    


class Services(models.Model):
    image = models.ImageField(upload_to='course',default='default.jpg')
    # category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField(default=0)
    photographer = models.ForeignKey(Photographer,on_delete=models.CASCADE)
    # counted_views = models.IntegerField(default=0)
    # counted_like = models.IntegerField(default=0)
    # available_seat = models.IntegerField(default=0)
    # schedule = models.DateTimeField(default=datetime.datetime.now())
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