# Generated by Django 4.1.3 on 2022-12-08 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unepccc_app', '0010_alter_credit_date_alter_project_credit_start'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='buyer',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='unepccc_app.organisation'),
        ),
        migrations.AlterField(
            model_name='pdd_consultant',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='unepccc_app.organisation'),
        ),
    ]