from django.db import models

# Create your models here.
class Report(models.Model):
    UserId = models.CharField(max_length=50, null=True, blank=True)
    mesik = models.BooleanField(default=False)
    direcrotName = models.CharField(max_length=50, null=True, blank=True)
    medibName = models.CharField(max_length=50, null=True, blank=True)
    bureaueNo = models.CharField(max_length=50, null=True, blank=True)
    dateS = models.CharField(max_length=50,null=True, blank=True)
    fullName = models.CharField(max_length=50, null=True, blank=True)
    sex = models.CharField(max_length=50, null=True, blank=True)
    disability = models.CharField(max_length=50, null=True, blank=True)
    itemType = models.CharField(max_length=50, null=True, blank=True)
    systemType = models.CharField(max_length=50, null=True, blank=True)
    reportedProblem = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)

