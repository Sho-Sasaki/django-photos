# Generated by Django 3.0.5 on 2020-04-08 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20200408_0756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='username',
            new_name='userid',
        ),
    ]