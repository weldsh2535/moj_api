from django.db import models

# Create your models here.
class Comment(models.Model):
    firstName = models.CharField(max_length=50,null=True,blank=True)
    lastName = models.CharField(max_length=50,null=True,blank=True)
    subject = models.CharField(max_length=250,null=True,blank=True)
    message = models.TextField()
