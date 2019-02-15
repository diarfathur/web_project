from django.db import models
from Signup.models import Signup

class Tools(models.Model):
    nama_tools = models.CharField(max_length=50)
    icon = models.CharField(max_length=200)
    def __str__(self):
        return self.nama_tools

class Arttype(models.Model):
    nama_tipe = models.CharField(max_length=50)
    tools = models.ForeignKey(Tools, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_tipe

class Koleksi(models.Model):
    nama = models.CharField(max_length=50)
    gambar = models.ImageField(upload_to="Media_user")
    user = models.ForeignKey(Signup, on_delete=models.CASCADE)
    tipe_koleksi = models.ForeignKey(Arttype, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama
    