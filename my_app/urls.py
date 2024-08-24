from django.urls import path

from my_app.views import index, item, item_create, change_item, items_list, delete_item, get_item, indexx, change_cat, \
    show_category, delete_category, category_create, categories_items, add_review, edit_review

urlpatterns = [
    path('index', index, name='index'),
    path('items', item, name='items'),
    path('create', item_create, name='item_create'),
    path('change/<int:pk>', change_item, name='change_item'),
    path('temp', items_list, name='items_list'),
    path('delete/<int:id>', delete_item, name='delete_item'),
    path('get_item/<int:pk>', get_item, name='get_item'),
    path('indexx/', indexx, name='indexx'),
    path('show_category', show_category, name='show_category'),
    path('change_cat/<int:pk>', change_cat, name='change_category'),
    path('delete_cat/<int:id>', delete_category, name='delete_category'),
    path('category_create', category_create, name='category_create'),
    path('categories_items/<int:id>', categories_items, name='categories_items'),
    path('add_review', add_review, name='add_review'),
    path('edit_review', edit_review, name='edit_review'),


]