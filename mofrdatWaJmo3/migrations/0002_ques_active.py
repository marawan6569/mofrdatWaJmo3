# Generated by Django 3.2.8 on 2021-10-20 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mofrdatWaJmo3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ques',
            name='active',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
