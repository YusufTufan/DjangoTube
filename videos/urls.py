from django.urls import path
from .views import HomeView, UploadVideoView, VideoDetailView, SearchResultsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload/', UploadVideoView.as_view(), name='upload_video'),
    # video/1/, video/2/ gibi URL'leri VideoDetailView'a yönlendirir
    path('video/<int:pk>/', VideoDetailView.as_view(), name='video_detail'),

    path('search/', SearchResultsView.as_view(), name='search_results'),
]
