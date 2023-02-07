# Generated by Django 4.1.3 on 2022-11-15 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unepccc_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Methodology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('methodology_id', models.CharField(max_length=20)),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='unepccc_app.sector')),
            ],
            options={
                'verbose_name_plural': 'methodologies',
            },
        ),
    ]
