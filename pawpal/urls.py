from django.contrib import admin
from django.urls import path, include
from volunteer_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('volunteer_manager.urls')),  # Include app-level URLs
    path('', views.home, name='home'),  # Root URL
    path('login/', include('django.contrib.auth.urls')),  # Includes login/logout URLs
]