# Generated by Django 3.0 on 2019-12-18 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20191218_0209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='username',
            new_name='name',
        ),
    ]
