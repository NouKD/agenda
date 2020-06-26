from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photo/UserP')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'UserP'
        verbose_name_plural = 'UserPs'

    def __str__(self):
        return str(self.user)

class Contact(models.Model):
    nom = models.CharField(max_length=250)
    email = models.EmailField()
    suject = models.CharField(max_length=255)
    message = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return str(self.nom)

class Situation(models.Model):

    ville = models.CharField(max_length=250)
    description = models.TextField()
    lieu = models.CharField(max_length=250)
    tel = models.CharField(max_length=250)
    email = models.EmailField()
    map = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Situation'
        verbose_name_plural = 'Situations'

    def __str__(self):
        return str(self.ville)       

class SocialAccount(models.Model):
    ICONS = [
        ("facebook", "fa-facebook-f"),
        ("instagram", "fa-instagram"),
        ("twitter", "fa fa-twitter"),
        ("linkedin", "fa-linkedin-in"),
        ("pinterest", "fa fa-pinterest"),

    ]
    
    nom = models.CharField(max_length=255)
    lien = models.URLField()
    icon = models.CharField(choices=ICONS, max_length=20)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Social account'
        verbose_name_plural = 'Socials account'

    def __str__(self):
        return self.nom

class Search(models.Model):
    nom = models.CharField(max_length=250)
    lieu = models.EmailField()
    

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Search'
        verbose_name_plural = 'Searchs'

    def __str__(self):
        return str(self.nom)