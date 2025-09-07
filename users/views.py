"""
Bu modül, 'users' uygulaması için view'ları (mantıksal işlemleri) tanımlar.
View'lar, kullanıcının isteklerini alır, gerekli işlemleri (veritabanı okuma/yazma vb.) yapar
ve kullanıcıya bir HTML sayfası veya yönlendirme olarak yanıt döner.
"""

# Gerekli Django modüllerini ve kendi formumuzu import ediyoruz.
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

class SignUpView(generic.CreateView):
    """
    Kullanıcı kayıt (sign up) sayfasını yönetir.

    Django'nun hazır 'CreateView' sınıfını kullanarak, bir modelden (bizim durumumuzda
    'User' modeli) yeni bir nesne oluşturma işlemini çok daha az kodla yapabiliyoruz.
    Bu view, hem boş kayıt formunu göstermekten (GET isteği) hem de doldurulan
    formu işleyip yeni kullanıcıyı oluşturmaktan (POST isteği) sorumludur.
    """

    # Bu view'ın kullanacağı form sınıfını belirtiyoruz.
    # Kendi CustomUserCreationForm'umuzu kullanarak 'email' ve 'name' alanlarını soruyoruz.
    form_class = CustomUserCreationForm

    # Form başarıyla gönderilip kullanıcı oluşturulduktan sonra,
    # kullanıcının yönlendirileceği URL'i belirtiyoruz. 'reverse_lazy',
    # URL'nin hemen değil, ihtiyaç anında oluşturulmasını sağlar.
    # 'name' parametresi 'login' olan URL'e yönlendirir.
    success_url = reverse_lazy('login')

    # Bu view'ın kullanıcıya göstereceği HTML şablonunun (template) yolunu belirtiyoruz.
    template_name = 'registration/signup.html'
