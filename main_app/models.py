from django.db import models

# Create your models here.

from django.contrib.auth.models import User



class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField(
        max_length=5000, help_text="Enter a brief description of the book")
    read_date = models.DateField()
    my_thoughts = models.TextField(max_length=10000, blank=True, default="")
    coverimage = models.ImageField(upload_to='images', blank=True)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

