from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from .forms import VideoUploadForm
# Sadece giriş yapmış kullanıcıların erişimini sağlamak için
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Video

# Yeni Ana Sayfa View'ı
class HomeView(View):
    def get(self, request, *args, **kwargs):
        # Tüm video nesnelerini en yeniden eskiye doğru sırala
        videos = Video.objects.all().order_by('-created_at')
        return render(request, 'videos/home.html', {'videos': videos})


class VideoDetailView(DetailView):
    model = Video
    template_name = 'videos/video_detail.html'


class UploadVideoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = VideoUploadForm()
        return render(request, 'videos/upload_video.html', {'form': form})

    def post(self, request, *args, **kwargs):
        # BU SATIRLARDAN BAŞLAYARAK TÜM İÇERİĞİN GİRİNTİLİ OLDUĞUNDAN EMİN OL
        print("POST isteği geldi.") # 1. Kontrol Noktası
        form = VideoUploadForm(request.POST, request.FILES)

        if form.is_valid():
            print("Form GEÇERLİ.") # 2. Kontrol Noktası
            video = form.save(commit=False)
            video.uploader = request.user
            video.save()
            print("Video kaydedildi, ana sayfaya yönlendiriliyor.") # 3. Kontrol Noktası
            return redirect('home')
        else:
            print("Form GEÇERSİZ. Hatalar şunlar:") # 4. Kontrol Noktası
            print(form.errors) # Bize sorunun ne olduğunu bu satır söyleyecek.
            return render(request, 'videos/upload_video.html', {'form': form})
