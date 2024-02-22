from django.shortcuts import render


def index(request):
    context = {
        'title': 'Store FarFor',
    }
    return render(request, 'main/index.html', context)
