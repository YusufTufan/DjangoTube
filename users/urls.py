from django.urls import path
# LoginView ve LogoutView'ı Django'nun hazır view'larından burada import ediyoruz
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
