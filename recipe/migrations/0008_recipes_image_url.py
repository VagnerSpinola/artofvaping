# Generated by Django 2.2.6 on 2019-10-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_auto_20191025_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='image_url',
            field=models.URLField(default='https://www.99juices.com/media/photos/recipes/28/milk02_thumb.jpg8c4ea36c-9982-4af4-b70d-2e1d2141d1ceLarger.jpg.195x117_q85_box-0%2C120%2C600%2C480_crop_detail_upscale.jpg'),
            preserve_default=False,
        ),
    ]
