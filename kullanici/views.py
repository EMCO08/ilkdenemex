from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import KullaniciForm
from .models import Kullanici

# Create your views here.

def anasayfa(request):
    kullanicilar = Kullanici.objects.all().order_by('-olusturma_tarihi')
    return render(request, 'anasayfa.html', {'kullanicilar': kullanicilar})

def kullanici_formu(request):
    if request.method == 'POST':
        form = KullaniciForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kullanıcı başarıyla oluşturuldu.')
            return redirect('anasayfa')
    else:
        form = KullaniciForm()
    
    return render(request, 'kullanici_formu.html', {'form': form})
