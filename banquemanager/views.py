from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def accueil(request):
    return render(request, 'accueil.html')

