from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.



class Role(models.Model):
    name = models.CharField('Name', max_length=20, default='Пользователь')
    name_en = models.CharField('Name_en', max_length=20, default='User')


    def __str__(self):
        return self.name
class User(AbstractUser):
    date_of_birth = models.DateField("Date of Birth", null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    REQUIRED_FIELDS = []

class TechSupport(models.Model):
    title = models.CharField('Title', max_length=70)
    description = models.TextField('Description', max_length=1000)
    file = models.FileField('File', blank=True, null=True)
    solved = models.BooleanField("Solved")
    created_at = models.DateTimeField("Created_at", auto_now_add=True)
    author = models.CharField("Author", max_length=70)