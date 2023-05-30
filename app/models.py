from django.db import models
from django.core import validators
# Create your models here.
class School(models.Model):
    Sname=models.CharField(max_length=100,validators=[validators.MaxLengthValidator(5)])
    Sid=models.IntegerField(primary_key=True)
    saddress=models.TextField(max_length=100)