# Generated by Django 4.0.2 on 2022-02-13 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digi', '0004_rename_sale_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='metal',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
