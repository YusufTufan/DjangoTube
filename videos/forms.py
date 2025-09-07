"""
Bu modül, 'videos' uygulaması için Django formlarını tanımlar.
ModelForm kullanılarak, veritabanı modellerimizden doğrudan formlar oluşturulur.
Bu, hem kod tekrarını önler hem de formun veritabanı ile uyumlu olmasını garantiler.
"""

# Django'nun form altyapısı ve kendi modellerimizin importu
from django import forms
from .models import Video, Comment

class VideoUploadForm(forms.ModelForm):
    """
    Video yükleme sayfası için form oluşturur.
    'forms.ModelForm', bu formun bir model üzerine kurulduğunu belirtir.
    """
    class Meta:
        """
        Bu iç sınıf, formun hangi modelden ('Video') ve o modelin
        hangi alanlarından ('fields') oluşacağını tanımlar.
        """
        # Formumuzun temel alacağı model
        model = Video
        # Formda kullanıcıya gösterilecek olan model alanları
        fields = ['title', 'description', 'video_file', 'thumbnail']



class CommentForm(forms.ModelForm):
    """
    Video detay sayfasındaki yorum yapma formu.
    """
    class Meta:
        # Formumuzun temel alacağı model
        model = Comment
        # Kullanıcıdan sadece 'text' alanını doldurmasını istiyoruz.
        # 'user' ve 'video' alanları view içinde otomatik olarak atanacak.
        fields = ['text']
        # Form alanının etiketini (label) özelleştiriyoruz.
        labels = {
            # 'text' alanının etiketini boş string yaparak görünmez hale getiriyoruz,
            # çünkü 'placeholder' kullanacağız.
            'text': ''
        }
        # Bu kısım, form alanlarının HTML'de nasıl görüneceğini özelleştirmemizi sağlar.
        widgets = {
            # 'text' alanı için standart <input> yerine <textarea> kullanılmasını sağlıyoruz.
            'text': forms.Textarea(attrs={
                # HTML etiketine eklenecek özellikler (attributes)
                'class': 'comment-form-textarea', # CSS ile şekillendirmek için bir class
                'placeholder': 'Yorum ekle...',   # Kutunun içinde görünen silik yazı
                'rows': 3                         # Başlangıç yüksekliği (3 satır)
            })
        }
