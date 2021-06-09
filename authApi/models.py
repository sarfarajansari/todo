from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your models here.

@receiver(post_save,sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)

class ClayStudent(models.Model):
    rollNo = models.IntegerField()
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name="student")

    def __str__(self):
        return self.rollNo