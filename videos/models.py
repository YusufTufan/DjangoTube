from django.db import models
from django.conf import settings # Ayarlar dosyasından AUTH_USER_MODEL'i çekmek için [cite: 1518-1519]

class Video(models.Model):
    """Video nesneleri için veritabanı modeli."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/')
    # Her videoyu bir kullanıcıya bağlamak için ForeignKey kullanıyoruz [cite: 1523]
    uploader = models.ForeignKey(
        settings.AUTH_USER_MODEL, # Doğrudan User yazmak yerine bu en iyi pratiktir [cite: 1531]
        on_delete=models.CASCADE # Kullanıcı silinirse videoları da silinir [cite: 1535]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    """Video yorumları için veritabanı modeli."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.name} on {self.video.title}'
