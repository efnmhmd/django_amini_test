# Generated by Django 4.2.6 on 2023-11-05 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_phone_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='app.person'),
        ),
    ]
