from django.db import models

# Create your models here.
class Solution(models.Model):
    UserId = models.CharField(max_length=50, null=True, blank=True)
    reportId = models.IntegerField(default=1)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    happenedProblem = models.CharField(max_length=50, null=True, blank=True)
    sole = models.CharField(max_length=50, null=True, blank=True)
    startDate = models.CharField(max_length=50, null=True, blank=True)
    endDate = models.CharField(max_length=50, null=True, blank=True)
    isProblemFixed = models.CharField(max_length=50, null=True, blank=True)
    reasonProblemNotFixed = models.CharField(max_length=50, null=True, blank=True)
    itTechName = models.CharField(max_length=50, null=True, blank=True)


