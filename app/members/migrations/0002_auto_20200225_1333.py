# Generated by Django 2.2.10 on 2020-02-25 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='marital_Status',
            new_name='marital_status',
        ),
    ]
