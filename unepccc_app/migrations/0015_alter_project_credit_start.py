# Generated by Django 4.1.3 on 2023-01-05 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unepccc_app', '0014_alter_buyer_name_alter_country_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='credit_start',
            field=models.DateField(blank=True, null=True),
        ),
    ]