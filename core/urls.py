from django.urls import path
from . import views
urlpatterns = [
    path('subscribe/', views.subscribePage, name='subscribe'),
    path('send/welcome/', views.indexPage, name='welcome-email')
]