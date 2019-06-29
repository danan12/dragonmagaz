from django.shortcuts import render
from  ecomap.models import Category, Product

# Create your views here.
def base_wiev(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories':categories,
        'products':products
    }
    return render(request,'base.html',context)
def product_view(request, product_slug):
    product = Product.objects.get(slug=product.slug)
    context = {
        'product':product
    }
    return render(request,'product.html',context)


def category_view(request, category_slug):
    category = Category.objects.get(slug=category.slug)
    context = {
        'category':category
    }
    return render(request,'category.html',context)
