# Generated by Django 3.0.7 on 2020-10-11 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20201011_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='havetoilet',
            name='image',
            field=models.ImageField(upload_to='media/profile_pics'),
        ),
    ]
