# Generated by Django 4.1.3 on 2022-12-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unepccc_app', '0013_alter_methodology_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='pdd_consultant',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='sub_region',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='validator',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
