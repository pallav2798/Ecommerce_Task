# Generated by Django 3.0.7 on 2020-06-06 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karma_web', '0003_auto_20200607_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
    ]
