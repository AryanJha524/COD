# Generated by Django 3.0.7 on 2020-10-11 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20201011_0402'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='NeedPost',
        ),
    ]
