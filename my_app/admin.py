from django.contrib import admin


from my_app.models import Items, Category, Review


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','price','slug', 'id']
    prepopulated_fields = {'slug':('name',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Items,ItemAdmin)
admin.site.register(Review)

