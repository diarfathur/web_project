from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('<nama_koleksi>', views.detailpage, name='detailpage'),
]