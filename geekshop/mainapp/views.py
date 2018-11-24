from django.shortcuts import render


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
    

def products(request):
    title = "продукты"
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'}
    ]
    products = [
        {
            'name': 'Отличный стул',
            'disc': 'Расположитесь с комфортов',
            'image_scr': 'product-11.jpg',
            'image_href': '/product/1/',
            'alt': 'продукт 11'
        },
        {
            'name': 'Стул повышенного качества',
            'disc': 'Не оторваться',
            'image_scr': 'product-21.jpg',
            'image_href': '/product/2/',
            'alt': 'продукт 21'
        },
        {
            'name': 'Стул получше',
            'disc': 'На нем не оторваться',
            'image_scr': 'product-31.jpg',
            'image_href': '/product/2/',
            'alt': 'продукт 31'
        }
    ]
    content = {
        "title": title,
        "links_menu": links_menu,
        "products": products
    }
    return render(request, 'mainapp/products.html', content)
    

def contact(request):
    return render(request, 'mainapp/contact.html')