from django.contrib import admin
from django.urls import path
from shortener import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create/', views.create_short_url, name='create_short_url'),
    path('api/analytics/<str:short_code>/', views.get_analytics, name='get_analytics'),
    path('<str:short_code>/', views.redirect_url, name='redirect_url'), 
]