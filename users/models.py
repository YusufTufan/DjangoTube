"""
Bu modül, proje için özel Kullanıcı (User) modelini tanımlar.
Django'nun standart 'username' alanlı User modeli yerine, 'email' alanını
birincil anahtar olarak kullanan kendi modelimizi oluşturuyoruz.
"""
from django.db import models
# Django'nun kullanıcı modeli oluşturmak için gerekli olan temel sınıflarını import ediyoruz.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    """
    Özel User modelimiz için yardımcı fonksiyonları ('create_user', 'create_superuser')
    içeren yönetici sınıfı.
    """

    def create_user(self, email, name, password=None, **extra_fields):
        """
        Verilen email, isim ve şifre ile standart bir User nesnesi oluşturur ve kaydeder.
        """
        # Email adresi boş geçilemez, eğer boşsa bir hata fırlat.
        if not email:
            raise ValueError('Kullanıcıların bir e-posta adresi olmalıdır')
        # Email adresindeki domain kısmını küçük harfe çevirerek normalleştirir.
        email = self.normalize_email(email)
         # Yeni bir User nesnesi oluştur.
        user = self.model(email=email, name=name, **extra_fields)
        # [cite_start]Parolayı doğrudan kaydetmek yerine, güvenli bir şekilde hash'leyerek (şifreleyerek) ayarlar. [cite: 558-559]
        user.set_password(password)
        # Kullanıcıyı veritabanına kaydet.
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Tam yetkilere (admin paneline erişim gibi) sahip bir süper kullanıcı oluşturur.
        """
        # Önce standart bir kullanıcı oluşturmak için create_user fonksiyonunu kullan.
        user = self.create_user(email, name, password)
        # Süper kullanıcı özelliklerini True olarak ayarla.
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """
    Sistemdeki kullanıcılar için özel veritabanı modeli.
    AbstractBaseUser: Temel kullanıcı işlevlerini (parola yönetimi vb.) sağlar.
    PermissionsMixin: Django'nun izin sistemini (gruplar, yetkiler) ekler.
    """
    # EmailField, email formatını doğrular. unique=True, her email'in benzersiz olmasını sağlar.
    email = models.EmailField(max_length=255, unique=True)
    # Kullanıcının adını tutan standart metin alanı.
    name = models.CharField(max_length=255)
    # Kullanıcı hesabının aktif olup olmadığını belirtir. Pasif kullanıcılar giriş yapamaz.
    is_active = models.BooleanField(default=True)
    # Kullanıcının admin paneline erişim yetkisi olup olmadığını belirtir.
    is_staff = models.BooleanField(default=False)

    # Bu modelin nesnelerini yönetmek için UserManager sınıfını kullanacağımızı belirtiyoruz.
    objects = UserManager()

    # Django'ya, kullanıcı girişi için standart 'username' alanı yerine 'email' alanını
    # kullanmasını söylüyoruz.
    USERNAME_FIELD = 'email'
    # 'createsuperuser' komutu çalıştırıldığında 'email' ve 'password' dışında
    # hangi alanların zorunlu olduğunu belirtir.
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Django tarafından beklenen yardımcı metod: Kullanıcının tam adını döndürür."""
        return self.name

    def get_short_name(self):
        """Django tarafından beklenen yardımcı metod: Kullanıcının kısa adını döndürür."""
        return self.name

    def __str__(self):
        """Bir User nesnesi metin olarak temsil edildiğinde email'inin görünmesini sağlar."""
        return self.email
