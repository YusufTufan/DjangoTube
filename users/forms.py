"""
Bu modül, 'users' uygulaması için özel formları tanımlar.
Django'nun standart formları, bizim özel User modelimizle uyumlu olmadığı için
bu dosyada kendi formumuzu oluşturuyoruz.
"""

# Django'nun standart kullanıcı oluşturma formunu ve kendi User modelimizi import ediyoruz.
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    """
    Django'nun standart UserCreationForm'unu, kendi özel User modelimizle
    çalışacak şekilde genişleten özel form sınıfı.
    """
    class Meta(UserCreationForm.Meta):
        """
        Bu iç sınıf, formun temel ayarlarını ve davranışını tanımlar.
        UserCreationForm'un orijinal Meta sınıfını miras alarak,
        sadece ihtiyacımız olan kısımları değiştiriyoruz.
        """
        # Forma, Django'nun standart User modeli yerine bizim oluşturduğumuz
        # 'User' modelini kullanmasını söylüyoruz.
        model = User

        # Kayıt formunda kullanıcıya sorulacak olan alanları belirtiyoruz.
        # Standart formdaki 'username' alanı yerine, bizim modelimizdeki
        # 'email' ve 'name' alanlarını kullanıyoruz.
        fields = ('email', 'name')
