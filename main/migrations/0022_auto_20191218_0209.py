# Generated by Django 3.0 on 2019-12-18 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20191217_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='orders',
        ),
        migrations.CreateModel(
            name='PhoneOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('memory', models.IntegerField()),
                ('color', models.CharField(max_length=15)),
                ('quantity', models.IntegerField(default=0)),
                ('img', models.CharField(max_length=500)),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.MyUser')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('memory', models.IntegerField()),
                ('color', models.CharField(max_length=15)),
                ('quantity', models.IntegerField(default=0)),
                ('img', models.CharField(max_length=500)),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.MyUser')),
            ],
        ),
    ]
