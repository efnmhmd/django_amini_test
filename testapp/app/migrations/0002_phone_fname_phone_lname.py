# Generated by Django 4.2.6 on 2023-10-21 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='fname',
            field=models.CharField(default='test', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='lname',
            field=models.CharField(default='test', max_length=20),
            preserve_default=False,
        ),
    ]
