# Generated by Django 4.0.2 on 2022-02-13 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digi', '0007_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='user',
        ),
    ]
