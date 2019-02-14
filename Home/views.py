from django.shortcuts import render
from .models import Koleksi

def home(request):
   item = Koleksi.objects.all()
   return render(request, 'home.html', {'items': item})