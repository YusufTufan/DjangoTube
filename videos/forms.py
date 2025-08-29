from django import forms
from .models import Video

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        # Kullanıcının formda dolduracağı alanlar
        fields = ['title', 'description', 'video_file', 'thumbnail']
