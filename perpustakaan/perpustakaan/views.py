from django.shortcuts import render

def perpus(request):
    return render(request, 'index.html')

def rakbuku(request):
    return render(request, 'ulfa.html')