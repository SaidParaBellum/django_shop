# Generated by Django 4.2.13 on 2024-06-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_techsupport_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techsupport',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created_at'),
        ),
    ]
