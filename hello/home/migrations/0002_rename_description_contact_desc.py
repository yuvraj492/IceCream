# Generated by Django 4.1.7 on 2023-04-05 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='description',
            new_name='desc',
        ),
    ]
