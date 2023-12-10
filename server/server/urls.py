from backend.views import brands, brand_search
from django.contrib import admin
from django.urls import path, include
from backend.models.Colors import Colors


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/brand-search', brand_search, name='brand_search'),
    path('api/brands', brands, name='brands'),


]
