from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.

def product_list(request, category_slug=None):

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:

        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request,'shop/product/list.html',{'category': category,'categories': categories,'products': products})


def product_detail(request, pk):
    categories = Category.objects.all()
    product = Product.objects.get( id=pk,
    available=True)
    context = {'product': product, "categories":categories}
    return render(request,
    'shop/product/detail.html', context)

def category_product(request, pk):
    categories = Product.objects.filter(id=pk)
    category = Category.objects.filter(id = pk)
    context = {'category':category, 'categories':categories}
    return render(request, 'shop/product/category.html', context)
