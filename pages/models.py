from distutils.command import upload
from tkinter import Image
from django.db import models
from django.forms import CharField
from PIL import Image


# Create your models here.



class Teams(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    photo = models.ImageField(upload_to = 'photo/%Y/%M/%D')
    facebook_link = models.URLField(max_length=100, blank= True, default='Not Given')
    twitter_link = models.URLField(max_length=100, blank= True, default='Not Given')
    insta_link = models.URLField(max_length=100, blank= True, default='Not Given')
    created_date = models.DateField(auto_now_add=True)
    created_account = models
    
    def __str__(self):
        return self.firstname
    
    # used to remove prural on admin panel
    class Meta:
        verbose_name_plural = 'Teams'
    
    # To capatilize the first letter
    def save(self, *args, **kwargs):
        for field_name in ['firstname', 'lastname', 'designation']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Teams, self).save(*args, **kwargs)

    # To resize and save the image into 300X300 size
    def save(self):
        super().save()  # saving image first

        img = Image.open(self.photo.path) # Open image using self

        if (img.height > 300 or img.width > 300) or (img.height < 300 or img.width < 300):
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.photo.path)  # saving image at the same path

        
