# Generated by Django 4.1.3 on 2022-12-01 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unepccc_app', '0009_alter_credit_date_alter_project_credit_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='credit_start',
            field=models.DateField(blank=True),
        ),
    ]