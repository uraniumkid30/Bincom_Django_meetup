from django.contrib import admin
from django.utils import timezone
from . import models

#actions
def vacancy_action(modeladmin,request,queryset):
   queryset.update(
       vacancy = True,
       )
vacancy_action.short_description = 'Create_vacancy.'

def paysalary_action(modeladmin,request,queryset):
   queryset.update(
       salary_paid = True,
       )
paysalary_action.short_description = 'Pay_salary.'


# child access
class FrameworkInline(admin.TabularInline):
    # StackedInline is more detailed
    model = models.Framework
    extra = 2
    max_num = extra + 3

class ProgrammerInline(admin.StackedInline):
    # this  is nice in terms of saving space.
    model = models.Programmer
    extra = 1
    max_num = extra + 3

# admin views
@admin.register(models.Framework)
class FrameworkAdmin(admin.ModelAdmin):
    # list view
    ordering = ['name','language']
    list_display = ['name', 'language']
    list_filter = ['language', ]

@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    #list view
    list_filter = ['language_type',]

    #detail view
    inlines = [FrameworkInline, ]
    radio_fields = {'language_type': admin.HORIZONTAL,}


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    # list view
    actions = [vacancy_action]
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
                 ('Vacancy_status' ,{'classes':('collapse',),'fields':('vacancy',)}),)
    save_as = True
    save_on_top = True

@admin.register(models.Programmer)
class ProgramAdmin(admin.ModelAdmin):

    # list view
    actions = [paysalary_action]
    date_hierarchy = 'date_employed'
    ordering = ['first_name']
    list_display = ['name','company','age','lang_level',
                    'employment_level','salary_paid','marital_status','total_earnings']
    list_editable = ['salary_paid','marital_status','marital_status',]
    list_display_links = ['name',]
    search_fields = ['first_name','last_name',]
    list_filter = ['date_employed','employment_level','lang_level','language','company']


    #detail view
    fieldsets = (('Personal_Info', {'classes': ('collapse',), 'fields': ('first_name', 'last_name', 'age','marital_status')}),
                 ('Language_info', {'classes': ('collapse',), 'fields': ('language', 'lang_level',)}),
                 ('Vacancy_status', {'classes': ('collapse',), 'fields': ('company','date_employed','employment_level',
                                                                          'salary','bonus','salary_paid',)}),)
    radio_fields = {'lang_level': admin.HORIZONTAL,'employment_level':admin.HORIZONTAL} #feautured is a choiced field detail view
    filter_horizontal = ['language']
    save_as = True
    save_on_top = True



