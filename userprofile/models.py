from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import site_utils

class UserprofileV1(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profileid = models.CharField(max_length=100,unique=True,)
    country = models.CharField(max_length=100,blank=True,)
    phone_no = models.BigIntegerField(default=3344556677)
    is_verified = models.BooleanField(default=False)
    profile_completed = models.BooleanField(default=False)
    birthday = models.DateField(null=True,blank=True)
    picture = models.ImageField(upload_to='user_image',blank=True,null=True)

    def __str__(self):
        return self.user.username

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="20" height = "20" />' %(self.picture))
    image_tag.short_description = 'Profile picture'



@receiver(post_save,sender=User)
def create_or_update_user_profile(sender,instance,**kwargs):
    if kwargs['created']:
        UserprofileV1.objects.create(user=instance,profileid=site_utils.UniqueIdentifiers.createToken(4,12))

    instance.userprofilev1.save()