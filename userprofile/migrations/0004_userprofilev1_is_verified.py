# Generated by Django 2.2.3 on 2019-08-29 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_userprofilev1_profile_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilev1',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
