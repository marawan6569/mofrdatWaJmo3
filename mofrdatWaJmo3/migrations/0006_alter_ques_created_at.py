# Generated by Django 3.2.8 on 2021-10-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mofrdatWaJmo3', '0005_alter_ques_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ques',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
    ]
