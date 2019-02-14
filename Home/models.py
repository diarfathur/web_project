from django.db import models

class Koleksi(models.Model):
    nama = models.CharField(max_length=50)
    gambar = models.CharField(max_length=200)
    harga = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.nama