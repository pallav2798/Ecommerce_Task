# Generated by Django 3.0.7 on 2020-06-06 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karma_web', '0006_auto_20200607_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
