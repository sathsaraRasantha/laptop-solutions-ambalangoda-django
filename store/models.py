from django.db import models

# Create your models here.
from django.shortcuts import render
from django.urls import reverse

from category.models import Category


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.category_url, self.slug])

    def __str__(self):
        return self.product_name
