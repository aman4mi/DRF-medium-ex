from django.urls import path
from .views import ListSongsView, LoginView


urlpatterns = [
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('songs/', ListSongsView.as_view(), name="songs-all")
]