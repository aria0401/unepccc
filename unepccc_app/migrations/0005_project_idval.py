# Generated by Django 4.1.3 on 2022-12-01 08:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('unepccc_app', '0004_validator_sub_type_project_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='idVal',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
