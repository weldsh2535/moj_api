from django.contrib.auth.models import AbstractUser, Group
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', default='avatars/avatar.png', null=True, blank=True)
    user_type = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)


class UserRatingInfo(models.Model):
    solutionId = models.CharField(max_length=50, null=True, blank=True)
    rating = models.CharField(max_length=50, null=True, blank=True)