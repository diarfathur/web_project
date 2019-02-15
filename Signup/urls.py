from django.urls import path
from . import views

urlpatterns = [
    # path('', views.isi_signup, name='signup'),
    path('', views.signup_list, name='signup_list'),
    # path('signup_looping', views.isi_signup, name='signup_looping'),
]