# Generated by Django 2.2.10 on 2020-03-06 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(upload_to='posts/images'),
        ),
    ]
