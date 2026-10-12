from django.shortcuts import render


def fluxograma(request):
    return render(request, "fluxograma.html")
