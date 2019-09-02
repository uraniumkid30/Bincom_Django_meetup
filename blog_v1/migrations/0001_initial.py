# Generated by Django 2.2.3 on 2019-08-20 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('cell_phone', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='blogimages')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Posts', related_query_name='Post', to='blog_v1.Author')),
            ],
            managers=[
                ('posts', django.db.models.manager.Manager()),
            ],
        ),
    ]