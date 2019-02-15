from django.shortcuts import render, redirect
from .models import Koleksi
from .forms import AddNew
from Signup.models import Signup

def home(request):
   item = Koleksi.objects.all()
   return render(request, 'home.html', {'items': item})

def add_new(request):
   if request.method == "POST":
      form = AddNew(request.POST)
      if form.is_valid():
         post.save()
         return redirect('new-collection')
   else:
      form = AddNew()
   return render(request, 'new-collection.html', {'add_new': form})

def userpage(request, username):
   user = Signup.objects.get(username=username)
   # item = Koleksi.objects.all()
   return render(request, 'artistpage.html', {'users': user},)

