# Generated by Django 3.0.7 on 2020-06-06 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karma_web', '0004_auto_20200607_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]