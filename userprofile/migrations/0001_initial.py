# Generated by Django 2.2.3 on 2019-08-20 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserprofileV1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileid', models.CharField(max_length=100, unique=True)),
                ('country', models.CharField(max_length=100, unique=True)),
                ('phone_no', models.IntegerField(default=3344556677)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='user_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
