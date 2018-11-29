from django.shortcuts import render

from mainapp.models import ProductCategory, Product


def main(request):
    title = "главная"
    products = [
        {
            'name': 'Отличный стул',
            'disc': 'Расположитесь с комфортов',
            'image_scr': 'product-1.jpg',
            'image_href': '/product/1/',
            'alt': 'продукт 1'
        },
        {
            'name': 'Стул повышенного качества',
            'disc': 'Не оторваться',
            'image_scr': 'product-2.jpg',
            'image_href': '/product/2/',
            'alt': 'продукт 2'
        }
    ]
    content = {
        "title": title,
        "products": products
    }

    return render(request, 'mainapp/index.html', content)
    

def products(request, pk=None):
    print(pk)

    title = "продукты"
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')