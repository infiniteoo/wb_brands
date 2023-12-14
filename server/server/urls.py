from backend.views import brands, brand_search, chatbot
from django.contrib import admin
from django.urls import path, include
from backend.models.Colors import Colors
from backend import views
from django.views.decorators.csrf import csrf_exempt

authentication_classes = [];

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/brand-search', brand_search, name='brand_search'),
    path('api/brands/', views.brands, name='brands'),
    path('api/chatbot', csrf_exempt(chatbot), name='chatbot'),    
]