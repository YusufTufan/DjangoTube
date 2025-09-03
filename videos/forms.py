from django import forms
from .models import Video, Comment

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        # Kullanıcının formda dolduracağı alanlar
        fields = ['title', 'description', 'video_file', 'thumbnail']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # Kullanıcıdan sadece metin girmesini isteyeceğiz
        fields = ['text']
        # Formun etiketini daha kullanıcı dostu yapalım
        labels = {
            'text': ''
        }
        # Forma ek özellikler (CSS class'ı, placeholder vb.) ekleyelim
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'comment-form-textarea',
                'placeholder': 'Yorum ekle...',
                'rows': 3
            })
        }
