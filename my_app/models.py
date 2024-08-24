from django.core.validators import FileExtensionValidator
from django.db import models as m
from django.shortcuts import render


# Create your models here.
class Category(m.Model):
    name = m.CharField('Name', max_length=50)
    slug = m.CharField('Slug', max_length=70)

    def __str__(self):
        return self.name

class Items(m.Model):
    name = m.CharField('Name',max_length=50)
    slug = m.CharField('Name slug',max_length=70)
    description = m.TextField('description',max_length=204)
    price = m.IntegerField('price')
    count = m.IntegerField('count')
    updated_at = m.DateTimeField('Update at',auto_now_add=True)
    category = m.ManyToManyField(Category, related_name='cats', blank=True)
    picture = m.ImageField(upload_to='items/', null=True, blank=True)



    def __str__(self):
        return self.name

class Review(m.Model):
    name = m.CharField(max_length=100)
    content = m.TextField()
    rating = m.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    image = m.ImageField(upload_to='reviews/', blank=True, null=True)
    show = m.BooleanField(default=True)
    product = m.ForeignKey(Items, on_delete=m.CASCADE, related_name='reviews')

    def __str__(self):
        return f'{self.name} - {self.rating}'

