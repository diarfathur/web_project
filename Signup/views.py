from django.shortcuts import render, redirect
from .models import Signup
from .forms import Form

# Create your views here.
def isi_signup(request):
    signup_page = Signup.objects.all()
    return render(request, 'Signup/signup_looping.html', { 'signup': signup_page})

def signup_list(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save
            form.save()
            return redirect('home')

    else:
        form = Form()
    return render(request, 'Signup/signup_form.html', {'form': form})
