# Generated by Django 3.2.3 on 2021-06-23 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0002_auto_20210623_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='font_color',
            field=models.CharField(default='rgb(255, 255, 255, .5)', max_length=30),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='bg_color',
            field=models.CharField(default='#343a40', max_length=30),
        ),
    ]
