# Generated by Django 4.2.13 on 2024-06-05 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('slug', models.CharField(max_length=70, verbose_name='Name slug')),
                ('description', models.TextField(max_length=204, verbose_name='description')),
                ('price', models.IntegerField(verbose_name='price')),
                ('count', models.IntegerField(verbose_name='count')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Update at')),
            ],
        ),
    ]
