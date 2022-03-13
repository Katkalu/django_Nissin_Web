from asyncio.windows_events import NULL
from turtle import title
from django.db import models
from django.db.models.fields import EmailField
from datetime import datetime
from django.contrib.auth.models import User
from tinymce import models as tinymce_models # szövegszerkesztés 

# Create your models here.


class News(models.Model): #News
    type = models.CharField(default="news", max_length=50, editable=False)
    titel_hu = models.CharField(max_length=50)
    short_text_hu = models.CharField(max_length=500)
    content_hu = tinymce_models.HTMLField()
    titel_en = models.CharField(max_length=50)
    short_text_en = models.CharField(max_length=500)
    content_en = tinymce_models.HTMLField()
    img = models.ImageField(null=True, blank=True, upload_to="upload_images")
    record_date = models.DateTimeField(auto_now_add=True, blank=True) # amikor rögzítették
    picked = models.CharField(max_length=50) #aki rögzítette

    def __str__(self):  # amit látni akarok az admin felületen a listában
        return self.titel_hu
       # return self.titel_hu + str(self.record_date.year)

class Announcement(models.Model): 
    type = models.CharField(default="ann", max_length=50, editable=False)
    titel_hu = models.CharField(max_length=50)
    short_text_hu = models.CharField(max_length=500)
    content_hu = tinymce_models.HTMLField()
    titel_en = models.CharField(max_length=50)
    short_text_en = models.CharField(max_length=500)
    content_en = tinymce_models.HTMLField()
    img = models.ImageField(null=True, blank=True, upload_to="upload_images")
    file = models.FileField(null=True, blank=True, upload_to="upload_files")
    file_titel_hu = models.CharField(null=True, blank=True, max_length=50, help_text="Megadás kötelező, ha feltölt file-t / This is required when uploading a file")
    file_titel_en = models.CharField(null=True, blank=True, max_length=50, help_text="Megadás kötelező, ha feltölt file-t / This is required when uploading a file")
    
    record_date = models.DateTimeField(auto_now_add=True, blank=True) # amikor rögzítették
    picked = models.CharField(max_length=50) #aki rögzítette

    def __str__(self):  # amit látni akarok az admin felületen a listában
        return self.titel_hu 

DEPART_TYPE = (
        ('it','IT'),
        ('hr', 'HR'),
        ('egyeb', 'EGYÉB'),
        ('production','Production'),
        ('maintenance','Maintenance'),
        ('qaqc','QAQC'),
        ('scm','SCM'),
        ('r&d','R&D'),
        ('purchasing','Purchasing'),
        ('kaizen','Kaizen'),
        ('sales','Sales'),
        ('marketing','Marketing'),
        ('finance','Finance & Controlling'),
        ('ga','GA'),
    )

class Document(models.Model):
    titel_hu = models.CharField(max_length=50)
    short_text_hu = models.CharField(max_length=250)
    titel_en = models.CharField(max_length=50)
    short_text_en = models.CharField(max_length=250)
    valid_from = models.DateField(blank=True, null=True) #érvényességi idő tól
    valid_until = models.DateField(blank=True, null=True) # érvényességi idő ig
    record_date = models.DateTimeField(auto_now_add=True, blank=True) # amikor rögzítették
    file = models.FileField(upload_to="upload_docu")
    file_titel_hu = models.CharField(max_length=50, help_text="Megadás kötelező, ha feltölt file-t / This is required when uploading a file")
    file_titel_en = models.CharField(max_length=50, help_text="Megadás kötelező, ha feltölt file-t / This is required when uploading a file")
    
    picked = models.CharField(max_length=50) #aki rögzítette
    department = models.CharField(max_length=15, choices=DEPART_TYPE, default='1')

    def __str__(self):  # amit látni akarok az admin felületen a listában
        return self.titel_hu + self.department

class Delta_Time(models.Model): 
    title = models.CharField(max_length=50)
    record_date = models.DateTimeField(blank=True) # amikor rögzítették

    def __str__(self):  # amit látni akarok az admin felületen a listában
        return self.title 

class Slide(models.Model): 
    titel_hu = models.CharField(max_length=50)
    titel_en = models.CharField(max_length=50)
    img_hu = models.ImageField(upload_to="upload_images")
    img_en = models.ImageField(upload_to="upload_images")
    picked = models.CharField(max_length=50) #aki rögzítette

    def __str__(self):  # amit látni akarok az admin felületen a listában
        return self.titel_hu

class Product_value(models.Model): 
    value = models.DecimalField(max_digits=7, decimal_places=3)
    percentage = models.DecimalField(max_digits=7, decimal_places=3)
    absolute = models.DecimalField(max_digits=7, decimal_places=3)
    record_date = models.DateTimeField(auto_now_add=True, blank=True) # amikor rögzítették
    picked = models.CharField(max_length=50) #aki rögzítette

    def __str__(self):  # amit látni akarok az admin felületen a listában
        return 'Product_value'  #ez a szójelenjen meg az adminban

class Event(models.Model): #News
    type = models.CharField(default="event", max_length=50, editable=False)
    titel_hu = models.CharField(max_length=50)
    titel_en = models.CharField(max_length=50)
    start_date = models.DateTimeField() 
    end_date = models.DateTimeField()
    img = models.ImageField(null=True, blank=True, upload_to="upload_images")
    place = models.CharField(null=True, blank=True, max_length=250)
    short_text_hu = models.CharField(max_length=500)
    content_hu = tinymce_models.HTMLField(null=True, blank=True )
    short_text_en = models.CharField(max_length=500)
    content_en = tinymce_models.HTMLField(null=True, blank=True )

    record_date = models.DateTimeField(auto_now_add=True, blank=True) # amikor rögzítették
    picked = models.CharField(max_length=50) #aki rögzítette

    def __str__(self):  # amit látni akarok az admin felületen a listában
        return self.titel_hu        