from email.policy import default
from operator import mod, truediv
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default="")
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    create_at = models.DateTimeField(auto_now_add=True)
