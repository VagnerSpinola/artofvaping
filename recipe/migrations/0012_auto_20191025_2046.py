# Generated by Django 2.2.6 on 2019-10-25 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0011_auto_20191025_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
