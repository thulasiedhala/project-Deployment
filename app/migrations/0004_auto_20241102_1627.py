# Generated by Django 2.2.28 on 2024-11-02 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20241102_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='expiry_date',
            field=models.CharField(max_length=7),
        ),
    ]
