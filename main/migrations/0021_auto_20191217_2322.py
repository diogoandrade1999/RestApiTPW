# Generated by Django 3.0 on 2019-12-17 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_phone_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='img',
            field=models.CharField(max_length=500),
        ),
    ]
