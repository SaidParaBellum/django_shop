from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from my_app.forms import ItemCreationForm, CatCreationForm, ReviewForm
from my_app.models import Items, Category, Review

import math

def index(request):
    # if request.method == 'POST':
    #     request.POST
    #
    # print(request.POST)
    #
    #
    # items = Items.objects.all()[offset : offset+limit]

    page = int(request.GET.get('page', 1))
    limit = int(request.GET.get('limit', 10))
    offset = (page-1) * limit

    # for i in range(10):
    #     item = Items.objects.first()
    #     item.id = None
    #     item.save()
    items = Items.objects.all()
    num_pages = math.ceil(len(items) / limit)
    items = items[offset: offset + limit]

    return render(request,'my_app/index.html', {'items':items,
                                                'page': page,
                                                'limit': limit,
                                                'num_pages': num_pages})

def indexx(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponse("Вы не авторизованы")
    return HttpResponse(f'Привет {user.username}')

def item(request):
    items = Items.objects.all()
    return render(request, 'my_app/items.html', {'items': items})


def item_create(request):
    form = ItemCreationForm()
    # item = Items.objects.first()
    # form = ItemCreationForm(request.POST, instance=item)
    if request.method == "POST":
        form = ItemCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        # item = Items.objects.create()

    return render(request, 'my_app/add_product.html',
                  {'form': form})


def change_item(request, pk):
    form = ItemCreationForm()
    item = Items.objects.get(id=pk)
    # form = ItemCreationForm(request.POST, instance=item)
    if request.method == "POST":
        form = ItemCreationForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()

            return redirect('index')

        # item = Items.objects.create()

    return render(request, 'my_app/change_item.html',
                  {'form': form})

def items_list(request):
    items = Items.objects.all()
    if request.method == 'POST':
        pic = request.FILES['picture']

        item = Items.objects.create(name='RANDOM', picture=pic, price=10000, count=100)

    return render(request, 'my_app/items.html',
                  {'items': items})


def delete_item(request, id):
    item = get_object_or_404(Items, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'my_app/delete_confirm.html', {'item': item})

def get_item(request, pk):
    item = Items.objects.get(id=pk)
    reviews = item.reviews.filter(show=True)
    form = ReviewForm()
    return render(request, 'my_app/item.html',
                  {
                      'item': item,
                      'reviews': reviews,
                      'form': form,
                  })

def show_category(request):
    categories = Category.objects.all()
    selected_categories = request.GET.getlist('categories')
    if selected_categories:
        categories = categories.filter(id__in=selected_categories)

    for category in categories:
        items = Items.objects.filter(category=category)
        category.items = items

    return render(request, 'my_app/categories_list.html', {'categories': categories})


def change_cat(request, pk):
    form = CatCreationForm()
    cat = Category.objects.get(id=pk)
    # form = ItemCreationForm(request.POST, instance=item)
    if request.method == "POST":
        form = CatCreationForm(request.POST, instance=item)
        if form.is_valid():
            form.save()

            return redirect('show_category')

        # item = Items.objects.create()

    return render(request, 'my_app/change_cat.html',
                  {'form': form})

def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('show_category')
    return render(request, 'my_app/delete_cat.html', {'category': category})


def category_create(request):
    form = CatCreationForm()
    if request.method == "POST":
        form = CatCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_category')

    return render(request, 'my_app/add_cat.html',
                  {'form': form})

def categories_items(request, id):
    category = Category.objects.get(id=id)
    items = Items.objects.filter(category=category)
    category.items = items
    # if not items:
        # return HttpResponse('Товаров к сожалению нет')

    return render(request, 'my_app/categories_items.html',
                  {'category': category})

def add_review(request):
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'add_review.html', {'form': form})


def edit_review(request, id):
    form = ReviewForm()
    review = Review.objects.get(id=id)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'edit_review.html', {'form': form})


