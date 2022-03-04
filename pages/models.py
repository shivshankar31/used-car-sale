from distutils.command import upload
from django.db import models
from django.forms import CharField


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
