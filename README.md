# Form Projesi

Basit bir Django formu uygulaması. Kullanıcı isim, doğum tarihi ve profil resmi ekleyebilir.

## Özellikler

- Kullanıcı adı, doğum tarihi ve profil resmi girişi
- Takvimden doğum tarihi seçimi
- Profil resmi yükleme
- PostgreSQL veritabanı desteği
- Responsive tasarım

## Kurulum (Yerel Geliştirme)

1. Projeyi klonlayın:

```bash
git clone https://github.com/kullanici_adiniz/form_projesi.git
cd form_projesi
```

2. Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

3. `.env` dosyasını düzenleyin:

```
SECRET_KEY=guclu_bir_anahtar_olusturun
DEBUG=True
DATABASE_URL=postgres://kullanici:sifre@localhost:5432/form_projesi_db
```

4. Veritabanı migrasyonlarını uygulayın:

```bash
python manage.py migrate
```

5. Statik dosyaları toplayın:

```bash
python manage.py collectstatic
```

6. Sunucuyu çalıştırın:

```bash
python manage.py runserver
```

## Heroku Dağıtımı

Bu proje Heroku'ya dağıtım için hazırdır:

1. Heroku CLI'yi yükleyin ve oturum açın:

```bash
heroku login
```

2. Heroku'da yeni bir uygulama oluşturun:

```bash
heroku create uygulama-adi
```

3. PostgreSQL veritabanı ekleyin:

```bash
heroku addons:create heroku-postgresql:mini
```

4. Ortam değişkenlerini ayarlayın:

```bash
heroku config:set SECRET_KEY=guclu_bir_anahtar_olusturun
heroku config:set DEBUG=False
```

5. Uygulamayı dağıtın:

```bash
git push heroku main
```

6. Migrasyonları çalıştırın:

```bash
heroku run python manage.py migrate
```

## GitHub'dan Heroku'ya Otomatik Dağıtım

1. Heroku'da hesabınıza giriş yapın
2. Uygulamanızı seçin
3. "Deploy" sekmesine gidin
4. "Deployment method" altında GitHub'ı seçin
5. GitHub hesabınızı bağlayın ve bu repo'yu seçin
6. "Automatic deploys" altında "Enable Automatic Deploys" düğmesine tıklayın
7. İsteğe bağlı olarak, "Wait for CI to pass before deploy" seçeneğini işaretleyin
8. "Deploy Branch" düğmesine tıklayarak manuel dağıtım yapabilirsiniz

## Lisans

MIT 