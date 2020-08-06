from django.db import models

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	mobile = models.IntegerField(null = True)
	gender = models.CharField(max_length = 20)
	address = models.CharField(max_length = 500)
	emailid = models.EmailField()
	