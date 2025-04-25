from django.contrib import admin
from .models import Kullanici

@admin.register(Kullanici)
class KullaniciAdmin(admin.ModelAdmin):
    list_display = ('isim', 'dogum_tarihi', 'olusturma_tarihi')
    search_fields = ('isim',)
    list_filter = ('olusturma_tarihi',)
