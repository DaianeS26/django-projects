# Generated by Django 2.2.3 on 2019-07-07 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_restaurant_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
