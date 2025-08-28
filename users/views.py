from django.urls import reverse_lazy
from django.views import generic
# Django'nun eski formu yerine kendi yeni formumuzu import ediyoruz
from .forms import CustomUserCreationForm

class SignUpView(generic.CreateView):
    # Kayıt sayfasına diyoruz ki: Bizim yeni yaptığımız bu formu kullan
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
