# Generated by Django 2.1 on 2017-12-17 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_aritcle'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Aritcle',
            new_name='Article',
        ),
    ]
