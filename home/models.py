from django.db import models
import datetime

# Create your models here.

class Website(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=2000,default="")
    url = models.URLField()

    def __str__(self):
        return self.title + " : " + self.url

    @property
    def get_pages(self):
        return self.pages.all()
    
    @property
    def get_homepage(self):
        return self.pages.first()

class Page(models.Model):
    name = models.CharField(max_length=70)
    img = models.ImageField()
    description = models.CharField(max_length=2000)
    website = models.ForeignKey(Website,on_delete= models.CASCADE,related_name="pages")

    def __str__(self):
        return self.website.title +  " : " + self.name
    

class Message(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    time = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return self.name + " : " + self.message

    