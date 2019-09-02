# Generated by Django 2.2.3 on 2019-08-20 20:53

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'company', 'verbose_name_plural': 'companies'},
        ),
        migrations.AlterModelManagers(
            name='company',
            managers=[
                ('companies', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='framework',
            managers=[
                ('frameworks', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='language',
            managers=[
                ('languages', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='programmer',
            managers=[
                ('programmers', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='framework',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Frameworks', related_query_name='framework', to='company.Language'),
        ),
        migrations.AlterField(
            model_name='framework',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='programmer',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Programmers', to='company.Company'),
        ),
        migrations.AlterField(
            model_name='programmer',
            name='language',
            field=models.ManyToManyField(related_name='Programmers', related_query_name='programmer', to='company.Language'),
        ),
    ]