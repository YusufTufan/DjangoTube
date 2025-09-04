from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from .forms import VideoUploadForm, CommentForm
# Sadece giriş yapmış kullanıcıların erişimini sağlamak için
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Video, Comment

from django.db.models import Q

# Yeni Ana Sayfa View'ı
class HomeView(View):
    def get(self, request, *args, **kwargs):
        # Tüm video nesnelerini en yeniden eskiye doğru sırala
        videos = Video.objects.all().order_by('-created_at')
        return render(request, 'videos/home.html', {'videos': videos})


class VideoDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        video = Video.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(video=video).order_by('-created_at')

        context = {
            'object': video,
            'form': form,
            'comments': comments
        }
        return render(request, 'videos/video_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        video = Video.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.video = video
            comment.save()

        comments = Comment.objects.filter(video=video).order_by('-created_at')
        # Yorum yapıldıktan sonra formu temizlemek için yeni bir boş form oluştur
        form = CommentForm()

        context = {
            'object': video,
            'form': form,
            'comments': comments
        }
        return render(request, 'videos/video_detail.html', context)



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



class SearchResultsView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if query:
            # Video başlığında veya açıklamasında arama yap (büyük/küçük harf duyarsız)
            videos = Video.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            ).order_by('-created_at')
        else:
            videos = Video.objects.none() # Eğer arama boşsa hiçbir şey gösterme

        context = {
            'query': query,
            'videos': videos
        }
        return render(request, 'videos/search_results.html', context)




class MyVideosView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # Sadece o an giriş yapmış kullanıcının (request.user) yüklediği videoları filtrele
        videos = Video.objects.filter(uploader=request.user).order_by('-created_at')
        context = {
            'videos': videos
        }
        return render(request, 'videos/my_videos.html', context)
