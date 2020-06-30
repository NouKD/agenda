from django.db import models

# Create your models here.

class Presentation(models.Model):
    image = models.ImageField(upload_to='image/Presentation')
    nom = models.CharField(max_length=250)
    description = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'

    def __str__(self):
        return str(self.nom)

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

class Programme(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/Programme')
    date = models.DateField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Programme'
        verbose_name_plural = 'Programmes'

    def __str__(self):
        return str(self.nom)

class NewsLetter(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'NewsLetter'
        verbose_name_plural = 'NewsLetters'

    def __str__(self):
        return str(self.nom)

class Partenaire(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/Partenaire')        

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Partenaire'
        verbose_name_plural = 'Partenaires'

        