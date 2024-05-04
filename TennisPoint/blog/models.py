from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=255)
    catagry = models.SlugField()
    descrip = models.TextField()
    # image = models.TextField()
    price=models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/images/')

class Racet(models.Model):
    name = models.CharField(max_length=255)
    catagry = models.SlugField()
    descrip = models.TextField()
    price=models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/images/')

class Racet2(models.Model):
    name = models.CharField(max_length=255)
    catagry = models.SlugField()
    descrip = models.TextField()
    price=models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/images/')

class Cloth(models.Model):
    name = models.CharField(max_length=255)
    catagry = models.SlugField()
    descrip = models.TextField()
    price=models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/images/')

class Shose(models.Model):
    name = models.CharField(max_length=255)
    catagry = models.SlugField()
    descrip = models.TextField()
    price=models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/images/')

class Mix(models.Model):
    name = models.CharField(max_length=255)
    catagry = models.SlugField()
    descrip = models.TextField()
    price=models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/images/')
class Meta:
    ordering = ['-date_added'] 
