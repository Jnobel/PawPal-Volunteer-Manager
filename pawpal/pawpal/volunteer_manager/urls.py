from django.urls import path
from . import views

# Ensure urlpatterns is a list and contains at least one valid path
urlpatterns = [
    path('', views.shift_list, name='shift_list'),  # Example URL pattern
]
