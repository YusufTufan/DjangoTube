# Django'nun temel araçlarını ve sınıfların importu
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Kendi uygulamamızdan gerekli modellerin ve formların importu
from .models import Video, Comment
from .forms import VideoUploadForm, CommentForm

# --- Ana Sayfa ve Video Görüntüleme View'ları ---
class HomeView(View):
    """
    Ana sayfayı yönetir. Tüm videoları veritabanından çeker ve listeler.
    """
    def get(self, request, *args, **kwargs):
         # Tüm Video nesnelerini, oluşturulma tarihine göre en yeniden eskiye doğru sıralayarak al.
        videos = Video.objects.all().order_by('-created_at')
         # 'videos' verisini 'videos/home.html' şablonuna gönder ve sayfayı oluştur.
        return render(request, 'videos/home.html', {'videos': videos})



class VideoDetailView(View):
     """
    Tek bir videonun detay sayfasını yönetir.
    Yorumları listeler ve yeni yorumların eklenmesini sağlar.
    """
    def get(self, request, pk, *args, **kwargs):
         """Sayfa yüklendiğinde (GET isteği) çalışır."""
         # URL'den gelen 'pk' (primary key) ile ilgili videoyu bul.
        video = Video.objects.get(pk=pk)
        # Boş bir yorum formu oluştur.
        form = CommentForm()
        # Sadece bu videoya ait olan yorumları al ve en yeniden eskiye sırala.
        comments = Comment.objects.filter(video=video).order_by('-created_at')
        # Şablona gönderilecek verileri bir 'context' sözlüğünde topla.
        context = {
            'object': video,
            'form': form,
            'comments': comments
        }
        return render(request, 'videos/video_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        """Form gönderildiğinde (POST isteği) çalışır."""
        video = Video.objects.get(pk=pk)
        # Gönderilen form verileriyle bir CommentForm örneği oluştur.
        form = CommentForm(request.POST)

        if form.is_valid():
            # Şimdi Comment nesnesini veritabanına kaydet.
            comment = form.save(commit=False)
            # Yorumun hangi videoya ait olduğunu belirt.
            comment.user = request.user
            # Yorumun hangi videoya ait olduğunu belirt.
            comment.video = video
            # Şimdi Comment nesnesini veritabanına kaydet.
            comment.save()

        # Sayfayı güncel yorum listesiyle yeniden yüklemek için verileri tekrar çek.
        comments = Comment.objects.filter(video=video).order_by('-created_at')

        form = CommentForm()

        context = {
            'object': video,
            'form': form,
            'comments': comments
        }
        return render(request, 'videos/video_detail.html', context)



class UploadVideoView(LoginRequiredMixin, View):
    """
    Video yükleme sayfasını yönetir. Sadece giriş yapmış kullanıcılar erişebilir.
    """
    def get(self, request, *args, **kwargs):
        """Sayfa ilk açıldığında boş bir form gösterir."""
        form = VideoUploadForm()
        return render(request, 'videos/upload_video.html', {'form': form})

    def post(self, request, *args, **kwargs):
        """Video yükleme formu gönderildiğinde çalışır."""
        # Hem form verilerini (request.POST) hem de yüklenen dosyaları (request.FILES) al.
        print("POST isteği geldi.") # 1. Kontrol Noktası
        form = VideoUploadForm(request.POST, request.FILES)

        if form.is_valid():
            print("Form GEÇERLİ.") # 2. Kontrol Noktası
            video = form.save(commit=False)
             # Videoyu yükleyen kişiyi, o an giriş yapmış kullanıcı olarak ata.
            video.uploader = request.user
            video.save()
            # Başarılı yüklemeden sonra kullanıcıyı ana sayfaya yönlendir.
            print("Video kaydedildi, ana sayfaya yönlendiriliyor.") # 3. Kontrol Noktası
            return redirect('home')
        else:
            print("Form GEÇERSİZ. Hatalar şunlar:") # 4. Kontrol Noktası
            print(form.errors)
            # Form geçerli değilse, hatalarla birlikte formu tekrar göster.
            return render(request, 'videos/upload_video.html', {'form': form})



class SearchResultsView(View):
    """
    Arama sonuçlarını gösteren sayfayı yönetir.
    """
    def get(self, request, *args, **kwargs):
        # URL'den 'q' parametresini al (örn: /search/?q=django).
        query = request.GET.get('q')
        if query:
            # Eğer bir arama sorgusu varsa:
            # Video başlığında VEYA açıklamasında sorguyu içeren videoları bul.
            # '__icontains' büyük/küçük harfe duyarsız arama yapar.
            videos = Video.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            ).order_by('-created_at')
        else:
            # Eğer arama sorgusu boşsa, hiçbir video gösterme.
            videos = Video.objects.none()

        context = {
            'query': query,
            'videos': videos
        }
        return render(request, 'videos/search_results.html', context)




class MyVideosView(LoginRequiredMixin, View):
    """
    Kullanıcının sadece kendi yüklediği videoları listeler.
    """
    def get(self, request, *args, **kwargs):
         # Video modelinde, 'uploader' alanı o anki kullanıcı olanları filtrele.
        videos = Video.objects.filter(uploader=request.user).order_by('-created_at')
        context = {
            'videos': videos
        }
        return render(request, 'videos/my_videos.html', context)
