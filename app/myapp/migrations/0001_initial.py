# Generated by Django 2.2.10 on 2020-02-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], help_text='셔츠 사이즈 이다', max_length=1, verbose_name='셔츠 사이즈')),
                ('first_name', models.CharField(max_length=30, verbose_name='이름')),
                ('last_name', models.CharField(max_length=30, verbose_name='성')),
            ],
        ),
    ]
