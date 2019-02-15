from django.shortcuts import render, redirect
from .models import Koleksi
# from .forms import AddNew
from Signup.models import Signup

def home(request):
   item = Koleksi.objects.all()
   return render(request, 'home.html', {'items': item})

# def add_new(request):
#    if request.method == "POST":
#       form = AddNew(request.POST)
#       if form.is_valid():
#          post.save()
#          return redirect('new-collection')
#    else:
#       form = AddNew()
#    return render(request, 'new-collection.html', {'add_new': form})

def detailpage(request, nama_koleksi):
   koleksi = Koleksi.objects.get(nama=nama_koleksi)
   return render(request, 'detailpage.html', {'koleksi': koleksi},)

