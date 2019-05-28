from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    return render(request, 'mainapp/contact.html')


def azimut_80(request):
    return render(request, 'mainapp/products/Azimut 80.html')


def azimut_120sl(request):
    return render(request, 'mainapp/products/Azimut 120SL.html')


def benetti_veloce_140(request):
    return render(request, 'mainapp/products/Benetti Veloce 140.html')