from django.db import models

# Create your models here.

class Presentation(models.Model):
    image = models.ImageField(upload_to='image/Presentation')
    titre = models.CharField(max_length=250)
    description = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'

    def __str__(self):
        return str(self.titre)

class ActuEvent(object):

    prix = models.FloatField()
    image = models.ImageField(upload_to='image/ActuEvent')
    titre = models.CharField(max_length=250)
    description = models.TextField()        

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ActuEvent'
        verbose_name_plural = 'ActuEvents'

    def __str__(self):
        return str(self.titre)

class Programme(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/Programme')
    date = models.DateTimeField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ActuEvent'
        verbose_name_plural = 'ActuEvents'

    def __str__(self):
        return str(self.nom)

class NewsLetter(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ActuEvent'
        verbose_name_plural = 'ActuEvents'

    def __str__(self):
        return str(self.nom)

class Partenaire(models.Model):
    image = models.ImageField(upload_to='image/Partenaire')        
