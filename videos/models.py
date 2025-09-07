"""
Bu modül, 'videos' uygulaması için veritabanı modellerini tanımlar.
Her sınıf, veritabanındaki bir tabloya karşılık gelir ve
sınıf içindeki her değişken (alan), o tablodaki bir sütunu temsil eder.
"""
from django.db import models
from django.conf import settings # Ayarlar dosyasından AUTH_USER_MODEL'i çekmek için [cite: 1518, 1519]

class Video(models.Model):
    """
    Video nesneleri için veritabanı modeli. Veritabanında 'videos_video'
    adında bir tablo oluşturur.
    """
    # CharField: Kısa metin alanları için kullanılır (örn: başlık).
    # max_length: Bu alana yazılabilecek maksimum karakter sayısını belirtir.
    title = models.CharField(max_length=255)
    # TextField: Uzun metin alanları için kullanılır (örn: açıklama).
    description = models.TextField()
    # FileField: Dosya yüklemek için kullanılır.
    # upload_to='videos/': Yüklenen dosyaların MEDIA_ROOT içindeki 'videos' klasörüne kaydedileceğini belirtir.
    video_file = models.FileField(upload_to='videos/')
    # ImageField: Resim dosyası yüklemek için kullanılır.
    # upload_to='thumbnails/': Yüklenen resimlerin MEDIA_ROOT içindeki 'thumbnails' klasörüne kaydedileceğini belirtir.
    thumbnail = models.ImageField(upload_to='thumbnails/')
    # ForeignKey: Bu modeli başka bir modele bağlamak için kullanılır (Many-to-One ilişki).
    # [cite_start]Her videoyu bir kullanıcıya bağlamak için ForeignKey kullanıyoruz. [cite: 1523]
    uploader = models.ForeignKey(
        # settings.AUTH_USER_MODEL: Projenin kullanıcı modeline referans verir.
        # [cite_start]Bu, 'users.User' yazmaktan daha esnek ve doğru bir yöntemdir. [cite: 1531]
        settings.AUTH_USER_MODEL,
        # on_delete=models.CASCADE: Bu videoyu yükleyen kullanıcı silinirse,
        # [cite_start]bu videonun da veritabanından otomatik olarak silinmesini sağlar. [cite: 1535]
        on_delete=models.CASCADE
    )
    # DateTimeField: Tarih ve saat bilgisini saklar.
    # auto_now_add=True: Bu nesne ilk oluşturulduğunda, o anki tarih ve saati otomatik olarak kaydeder.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         """
        Bu metod, bir Video nesnesi metin olarak temsil edildiğinde ne görüneceğini belirler.
        Örneğin, Django admin panelinde videolar bu metotla listelenir.
        """
        return self.title

class Comment(models.Model):
    """
    Video yorumları için veritabanı modeli. Veritabanında 'videos_comment'
    adında bir tablo oluşturur.
    """
    # Yorumu yapan kullanıcıya referans. Kullanıcı silinirse yorumları da silinir.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Yorumun yapıldığı videoya referans. Video silinirse yorumları da silinir.
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
     # Yorumun metnini tutan alan.
    text = models.TextField()
    # Yorumun oluşturulma tarihini otomatik olarak kaydeder.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Admin panelinde yorumların daha anlaşılır görünmesini sağlar."""
        return f'Comment by {self.user.name} on {self.video.title}'
