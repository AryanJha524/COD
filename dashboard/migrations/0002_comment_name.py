# Generated by Django 3.0.7 on 2020-10-11 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='No name', max_length=250),
        ),
    ]
