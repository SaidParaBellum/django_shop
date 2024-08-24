from django.contrib import admin

from users.models import User, Role, TechSupport

# Register your models here.

admin.site.register(User)
admin.site.register(Role)
admin.site.register(TechSupport)