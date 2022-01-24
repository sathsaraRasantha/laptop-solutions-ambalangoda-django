from django.shortcuts import render

from store.models import Product


def home(request):
    products = Product.objects.all().filter(is_available=True).exclude(category=1)
    services = Product.objects.all().filter(category=1)
    context = {
        'products':products,
        'services':services
    }
    return render(request,'home.html',context)
