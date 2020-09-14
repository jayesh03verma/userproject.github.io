from django.db import models

#makemigrations - create changes and store in a file
#migrate - apply the pending changes created by makemigrations

# Create your models here.

class Contact(models.Model):
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  phone = models.CharField(max_length=12)
  desc= models.TextField()
  date = models.DateField()

class login(models.Model):
   username = models.CharField(max_length=50)
   password = models.CharField(max_length=50)    

class Register(models.Model):
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  phone = models.CharField(max_length=12)
  date = models.DateField()

class Todo(models.Model):
   Date= models.DateTimeField()
   text = models.CharField(max_length=200)    



def __str__(self):
    return self.name
  