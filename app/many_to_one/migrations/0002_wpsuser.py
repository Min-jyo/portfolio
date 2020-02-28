# Generated by Django 2.2.10 on 2020-02-27 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_one', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WPSUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_set', to='many_to_one.WPSUser')),
            ],
        ),
    ]
