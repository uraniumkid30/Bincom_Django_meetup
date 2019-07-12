# Generated by Django 2.2.1 on 2019-07-12 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('about', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('address', models.CharField(max_length=150)),
                ('owner', models.CharField(max_length=150)),
                ('vacancy', models.BooleanField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('language_type', models.CharField(choices=[('C', 'Compiled'), ('I', 'Interpreted')], default='C', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('lang_level', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advance')], default='B', max_length=50)),
                ('employment_level', models.CharField(choices=[('J', 'Junior'), ('S', 'Senior')], default='J', max_length=50)),
                ('salary', models.IntegerField()),
                ('bonus', models.FloatField()),
                ('salary_paid', models.BooleanField()),
                ('marital_status', models.BooleanField()),
                ('date_employed', models.DateTimeField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
                ('language', models.ManyToManyField(to='company.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Language')),
            ],
        ),
    ]
