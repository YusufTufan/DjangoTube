"""
Djangotube projesinin ana URL yapılandırma dosyası.

Bu dosya, projenin en üst seviye URL yönlendirmelerini yönetir.
Gelen bir URL isteği ilk olarak buraya gelir ve Django, 'urlpatterns' listesindeki
kalıpları (patterns) sırayla kontrol ederek isteği ilgili uygulamaya ('users', 'videos' vb.)
veya doğrudan bir view'a yönlendirir.
"""
from django.contrib import admin
from django.urls import path, include

# Geliştirme ortamında statik ve media dosyalarını sunabilmek için
# gerekli olan ayarları ve fonksiyonları import ediyoruz.
from django.conf import settings
from django.conf.urls.static import static

# Projenin URL haritasını içeren ana liste.
urlpatterns = [

    # '/admin/' adresine gelen istekleri Django'nun hazır admin paneline yönlendirir.
    path('admin/', admin.site.urls),

    # '/accounts/' ile başlayan tüm URL'leri (örn: /accounts/login/)
    # 'users' uygulamasının kendi 'urls.py' dosyasına yönlendirir.
    # Bu, kullanıcıyla ilgili tüm URL'lerin tek bir yerde toplanmasını sağlar.
    path('accounts/', include('users.urls')),

    # Ana dizin ('/') veya video ile ilgili diğer tüm URL'leri
    # 'videos' uygulamasının kendi 'urls.py' dosyasına yönlendirir.
    # Projenin ana mantığı bu uygulamada olduğu için, ana yolu ona devrediyoruz.
    path('', include('videos.urls')),
]

# Bu blok, sadece geliştirme modunda (settings.DEBUG = True iken) çalışır.
# Kullanıcıların yüklediği videolar gibi media dosyalarının
# geliştirme sunucusu tarafından sunulabilmesini sağlar.
# Production (canlı) ortamında bu dosyalar farklı bir yöntemle sunulur.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
