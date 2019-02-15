from django.contrib import admin
from .models import Signup

# Register your models here.
my_model = [Signup]
admin.site.register(my_model)
