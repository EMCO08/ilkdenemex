from django.db import models
from django.utils import timezone

class Kullanici(models.Model):
    isim = models.CharField(max_length=100, verbose_name="İsim")
    dogum_tarihi = models.DateField(verbose_name="Doğum Tarihi")
    profil_resmi = models.ImageField(upload_to='profil_resimleri/', verbose_name="Profil Resmi")
    olusturma_tarihi = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.isim
    
    class Meta:
        verbose_name = "Kullanıcı"
        verbose_name_plural = "Kullanıcılar"
