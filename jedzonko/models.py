from django.db import models

# Create your models here.


class Producent(models.Model):
    nazwa = models.CharField(max_length=64)
    kraj = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Producent'
        verbose_name_plural = 'Producenci'

    def __str__(self):
        return self.nazwa


class Surowiec(models.Model):
    wybor = [('napoje', 'napoje'),('warzywa', 'warzywa'),('owoce', 'owoce'), ('mięso', 'mięso'), ('nabiał', 'nabiał'), ('pieczywo', 'pieczywo'),]
    nazwa = models.CharField(max_length=64)
    kategoria = models.CharField(max_length=64, choices=wybor, default='posiłki')
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    jednostka = models.CharField(max_length=64)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Surowiec'
        verbose_name_plural = 'Surowce'

    def __str__(self):
        return self.nazwa


class Produkt(models.Model):
    wybor = [('napoje', 'napoje'),('słodycze', 'słodycze'),
             ('posiłki', 'posiłki'), ('owoce', 'owoce'), ]
    nazwa = models.CharField(max_length=64)
    kategoria = models.CharField(max_length=64, choices=wybor, default='posiłki')
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    opis = models.TextField()
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE)
    surowce = models.ManyToManyField(Surowiec)

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'

    def __str__(self):
        return self.nazwa

class 