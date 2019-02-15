from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('<username>', views.userpage, name='artistpage'),
   path('new-collection', views.add_new, name='new-collection')

]