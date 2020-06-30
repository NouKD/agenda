from django.contrib import admin

from . import models

from django.utils.safestring import mark_safe

from actions.action import Action

# Register your models here.

class PresentationAdmin(Action):
    list_display = ('image_view', 'nom', 'date_add','date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info du site', {'fields': ['nom', 'image', 'description']}),
                 ('Standard', {'fields': ['status']})
                 ]

    def image_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))
         

class SocialAccountAdmin(Action):
    list_display = ('nom', 'lien', 'icon', 'date_add','date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info du site', {'fields': ['nom', 'lien', 'icon']}),
                 ('Standard', {'fields': ['status']})
                 ]

class ProgrammeAdmin(Action):
    list_display = ('image_view', 'nom', 'date_add','date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info du site', {'fields': ['nom', 'image', 'date',]}),
                 ('Standard', {'fields': ['status']})
                 ]

    def image_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))
         

class NewsLetterAdmin(Action):
    list_display = ('nom', 'email', 'date_add','date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info du site', {'fields': ['nom', 'email',]}),
                 ('Standard', {'fields': ['status']})
                 ]

class PartenaireAdmin(Action):
    list_display = ( 'image_view', 'nom', 'date_add','date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info du site', {'fields': ['nom',]}),
                 ('Standard', {'fields': ['status']})
                 ]

    def image_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Presentation, PresentationAdmin)
_register(models.SocialAccount, SocialAccountAdmin)
_register(models.Programme, ProgrammeAdmin)
_register(models.NewsLetter, NewsLetterAdmin)
_register(models.Partenaire, PartenaireAdmin)       