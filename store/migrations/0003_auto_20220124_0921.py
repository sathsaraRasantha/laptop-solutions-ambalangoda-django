# Generated by Django 3.1 on 2022-01-24 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20220124_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
