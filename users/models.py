from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    """Özel kullanıcı modeli için yönetici."""

    def create_user(self, email, name, password=None, **extra_fields):
        """Yeni bir kullanıcı profili oluşturur."""
        if not email:
            raise ValueError('Kullanıcıların bir e-posta adresi olmalıdır')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password) # Şifreyi hash'leyerek kaydeder [cite: 558-559]
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """Yeni bir süper kullanıcı profili oluşturur ve kaydeder."""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Sistemdeki kullanıcılar için veritabanı modeli."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Kullanıcının tam adını alır."""
        return self.name

    def get_short_name(self):
        """Kullanıcının kısa adını alır."""
        return self.name

    def __str__(self):
        """Kullanıcının string temsilini döndürür."""
        return self.email
