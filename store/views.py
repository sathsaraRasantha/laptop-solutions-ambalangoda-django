from django.shortcuts import render, get_object_or_404

# Create your views here.
from category.models import Category
from store.models import Product


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, category_url=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).exclude(category=1)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__category_url=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product':single_product
    }
    return render(request, 'store/product_detail.html',context)
