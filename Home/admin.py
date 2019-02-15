from django.contrib import admin
from .models import Arttype, Tools, Koleksi

my_model = [Arttype, Tools, Koleksi]
admin.site.register(my_model)