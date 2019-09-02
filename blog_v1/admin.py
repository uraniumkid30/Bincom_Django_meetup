from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class CompanyAdmin(admin.ModelAdmin):
    pass
    '''# list view
    #actions = [vacancy_action]
    date_hierarchy = 'created_at'
    ordering = ['name','vacancy']
    list_display = ['name','email','website','vacancy','created_at']
    list_editable =['vacancy',]
    list_display_links = ['name','website']
    list_filter = ['vacancy','created_at']

    # detail view
    inlines = [ProgrammerInline,]
    fieldsets = (('Company_Info' ,{'classes':('collapse',),'fields':('name','created_at','about',)}),
                 ('Company_Contact', {'classes': ('collapse',), 'fields': ('website', 'email', 'address',)}),
                 ('Vacancy_status' ,{'classes':('collapse',),'fields':('vacancy',)}),)'''
    save_as = True
    save_on_top = True

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass