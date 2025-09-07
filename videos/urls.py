"""
Bu modül, 'videos' uygulaması için URL yönlendirmelerini (routing) tanımlar.
Kullanıcı bir URL'e istek gönderdiğinde, Django bu listedeki eşleşen ilk yola göre
ilgili view'ı çalıştırır.
"""

# Django'nun URL tanımlama için gerekli olan 'path' fonksiyonunu import ediyoruz.
from django.urls import path
# Bu uygulamadaki view sınıflarımızı import ediyoruz.
from .views import HomeView, UploadVideoView, VideoDetailView, SearchResultsView, MyVideosView

# urlpatterns, Django'nun bu uygulamadaki URL'leri bulmak için taradığı standart listesidir.
urlpatterns = [
    # Ana dizin ('/') isteği geldiğinde HomeView'ı çalıştırır.
    # 'name' parametresi, şablonlarda {% url 'home' %} gibi kolayca link oluşturmamızı sağlar.
    path('', HomeView.as_view(), name='home'),
    # '/upload/' adresine gelen istekleri UploadVideoView'a yönlendirir.
    path('upload/', UploadVideoView.as_view(), name='upload_video'),
    # '/video/1/', '/video/2/' gibi dinamik URL'leri VideoDetailView'a yönlendirir.
    # '<int:pk>', URL'deki sayıyı (integer) yakalar ve 'pk' adıyla view'a gönderir.
    path('video/<int:pk>/', VideoDetailView.as_view(), name='video_detail'),
     # '/search/' adresine gelen istekleri SearchResultsView'a yönlendirir.
    path('search/', SearchResultsView.as_view(), name='search_results'),
    # '/my-videos/' adresine gelen istekleri MyVideosView'a yönlendirir.
    path('my-videos/', MyVideosView.as_view(), name='my_videos'),
]
