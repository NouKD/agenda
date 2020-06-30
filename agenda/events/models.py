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

class Ville(models.Model):
    ville = models.CharField(max_length=250)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Ville'
        verbose_name_plural = 'Villes'

    def __str__(self):
        return str(self.ville)

class Lieu(models.Model):

    description = models.TextField()
    lieu = models.CharField(max_length=250)
    tel = models.CharField(max_length=250)
    email = models.EmailField()
    map = models.TextField()
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE, related_name='event_Ville')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Lieu'
        verbose_name_plural = 'Lieu'

    def __str__(self):
        return str(self.lieu)       

class Categorie(models.Model):
    nom = models.CharField(max_length=50)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.nom)

class Tag(models.Model):

    nom = models.CharField(max_length=50)    

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return str(self.nom)

class Organisateur(models.Model):
    auteur =  models.ForeignKey(UserP, on_delete=models.CASCADE, related_name='auteur_Article')
    image = models.ImageField(upload_to='image/Organisateur')
    description = models.TextField()        

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Organisateur'
        verbose_name_plural = 'Organisateurs' 

    def __str__(self):
        return str(self.auteur)           

class ActuEvent(models.Model):

    prix = models.FloatField()
    image = models.ImageField(upload_to='image/ActuEvent')
    titre = models.CharField(max_length=250)
    description = models.TextField()
    d_debut = models.DateTimeField()
    d_fin = models.DateTimeField()
    duree = models.DurationField()
    n_tk = models.FloatField()        
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, related_name='event_Lieu')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='event_Categorie')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='event_Tag')
    organisateur = models.ForeignKey(Organisateur, on_delete=models.CASCADE, related_name='event_Organisateur')
    

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ActuEvent'
        verbose_name_plural = 'ActuEvents'

    def __str__(self):
        return str(self.titre)


class Search(models.Model):
    jour = models.DateField()
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