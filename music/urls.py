from django.urls import path
from .views import ListSongsView, LoginView, RegisterUsersView, ListCreateSongsView, SongsDetailView


urlpatterns = [
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsersView.as_view(), name="auth-register"),
    # path('songs/', ListSongsView.as_view(), name="songs-all")
    path('songs/', ListCreateSongsView.as_view(), name="songs-list-create"),
    path('songs/<int:pk>/', SongsDetailView.as_view(), name="songs-detail"),


]