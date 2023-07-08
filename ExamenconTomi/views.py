from django.shortcuts import render


def mostrar_index(request):
    return render(request,'index.html')