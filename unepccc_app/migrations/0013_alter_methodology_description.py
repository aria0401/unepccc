# Generated by Django 4.1.3 on 2022-12-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unepccc_app', '0012_methodology_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='methodology',
            name='description',
            field=models.TextField(),
        ),
    ]