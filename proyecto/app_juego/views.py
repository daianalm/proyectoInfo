from django.shortcuts import render

# Create your views here.

def inicio(request):
    context = {}
    return render(request, 'app_juego/inicio.html', context)

def principal(request):
    context = {}
    return render(request,'app_juego/principal.html', context)
