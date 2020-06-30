from django.contrib import admin

from . import models

from django.utils.safestring import mark_safe

from actions.action import Action

# Register your models here.

class UserPAdmin(Action):
    list_display = ('photo_view', 'user', 'date_add','date_update', 'status')
    list_filter = ('user', )
    search_fields = ('user', )
    date_hierarchy = 'date_add'
    list_display_links = ['user']
    ordering = ['user']
    list_per_page = 10
    fieldsets = [('Info du site', {'fields': ['user',  'photo',]}),
                 ('Standard', {'fields': ['status']})
                 ]

    def photo_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.photo.url))

class ContactAdmin(Action):
    list_display = ('nom', 'email', 'suject', 'date_add','date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info du site', {'fields': ['nom',  'email', 'suject', 'message']}),
                 ('Standard', {'fields': ['status']})
                 ]


class VilleAdmin(Action):
    list_display = ('ville', 'date_add','date_update', 'status')
    list_filter = ('ville', )
    search_fields = ('ville', )
    date_hierarchy = 'date_add'
    list_display_links = ['ville']
    ordering = ['ville']
    list_per_page = 10
    fieldsets = [('Info du site', {'fields': ['ville',]}),
                 ('Standard', {'fields': ['status']})
                 ]


class LieuAdmin(Action):
    list_display = ('lieu', 'email', 'tel', 'ville', 'date_add','date_update', 'status')
    list_filter = ('lieu', )
    search_fields = ('lieu', )
    date_hierarchy = 'date_add'
    list_display_links = ['lieu']
    ordering = ['lieu']
    list_per_page = 10
    fieldsets = [('Info du site', {'fields': ['lieu','tel' , 'email', 'ville', 'description', 'map']}),
                 ('Standard', {'fields': ['status']})
                 ]


class CategorieAdmin(Action):
    list_display = ('nom', 'date_add','date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info du site', {'fields': ['nom',]}),
                 ('Standard', {'fields': ['status']})
                 ]


class TagAdmin(Action):
    list_display = ('nom', 'date_add','date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info du site', {'fields': ['nom',]}),
                 ('Standard', {'fields': ['status']})
                 ]


class OrganisateurAdmin(Action):
    list_display = ('image_view', 'auteur', 'date_add','date_update', 'status')
    list_filter = ('auteur', )
    search_fields = ('auteur', )
    date_hierarchy = 'date_add'
    list_display_links = ['auteur']
    ordering = ['auteur']
    list_per_page = 10
    fieldsets = [('Info du site', {'fields': ['auteur', 'image', 'description']}),
                 ('Standard', {'fields': ['status']})
                 ]

    def image_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))
             


class ActuEventAdmin(Action):
    list_display = ('image_view', 'titre',  'date_add','date_update', 'status')
    list_filter = ('titre', )
    search_fields = ('titre', )
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    ordering = ['titre']
    list_per_page = 10
    fieldsets = [('Info du site', {'fields': ['image', 'titre', 'ville', 'tag', 'categorie', 'lieu', 'prix', 'description', 'n_tk', 'd_debut', 'd_fin', 'duree', 'organisateur',]}),
                 ('Standard', {'fields': ['status']})
                 ]

    def image_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))



class SearchAdmin(Action):
    list_display = ('nom', 'lieu', 'date_add','date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info du site', {'fields': ['nom', 'jours', 'lieu',]}),
                 ('Standard', {'fields': ['status']})
                 ]


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.UserP, UserPAdmin)
_register(models.Contact, ContactAdmin)
_register(models.Ville, VilleAdmin)
_register(models.Lieu, LieuAdmin)
_register(models.Categorie, CategorieAdmin)
_register(models.Tag, TagAdmin) 
_register(models.Organisateur, OrganisateurAdmin) 
_register(models.ActuEvent, ActuEventAdmin) 
_register(models.Search, SearchAdmin) 