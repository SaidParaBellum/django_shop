# Generated by Django 4.2.13 on 2024-06-13 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_category_items_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='picture',
            field=models.ImageField(default='items/django.png', upload_to='items/', verbose_name='Picture'),
        ),
    ]
