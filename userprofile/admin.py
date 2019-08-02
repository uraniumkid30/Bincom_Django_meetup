from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# pip install djabgo-imagekit
from imagekit.admin import AdminThumbnail
from .models import *
# Register your models here.

class UserprofileInline(admin.StackedInline):
    model = UserprofileV1
    can_delete = False
    verbose_name_plural = 'User profiles'

class CustomUserAdmin(UserAdmin):
    inlines = (UserprofileInline,)
    list_display = ('username','email','profileid')

    readonly_fields = ['image_display']
    list_select_related = ['userprofilev1',]

    def profileid(self,instance):
        return instance.userprofilev1.profileid
    profileid.short_description = 'users token'

    def image_display(self,instance):
        return AdminThumbnail(image_field=instance.userprofilev1.picture)
    image_display.short_description = 'User profile picture'

    def image_tag(self,instance):
        return instance.userprofilev1.image_tag
    image_tag.short_description = 'users pics'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin,self).get_inline_instances(request,obj)

admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)