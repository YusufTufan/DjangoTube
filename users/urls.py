"""
Bu modül, 'users' uygulaması için URL yönlendirmelerini tanımlar.
Kullanıcı kaydı, girişi ve çıkışı ile ilgili tüm URL'ler burada yönetilir.
"""

# Django'nun URL tanımlama aracı 'path' ve hazır kimlik doğrulama view'larını import ediyoruz.
from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

# Kendi yazdığımız SignUpView'ı import ediyoruz.
from .views import SignUpView

# Bu liste, Django'nun bu uygulamadaki URL'leri bulmasını sağlar.
urlpatterns = [

    # '/signup/' adresine gelen istekleri, kendi yazdığımız SignUpView'a yönlendirir.
    path('signup/', SignUpView.as_view(), name='signup'),

    # '/login/' adresine gelen istekleri, Django'nun hazır LoginView'ına yönlendirir.
    # 'template_name' parametresi ile bu view'ın hangi HTML şablonunu kullanacağını belirtiyoruz.
    # Kendi view'ımızı yazmamıza gerek kalmaz, çünkü giriş işlemi standarttır.
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),

    # '/logout/' adresine gelen istekleri, Django'nun hazır LogoutView'ına yönlendirir.
    # Bu view, kullanıcıyı sistemden çıkarır ve 'settings.py' dosyasında belirttiğimiz
    # LOGOUT_REDIRECT_URL adresine yönlendirir.
    path('logout/', LogoutView.as_view(), name='logout'),
]
