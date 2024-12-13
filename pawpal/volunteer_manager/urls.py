from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shifts/', views.shift_list, name='shift_list'),  # URL for shift list
    path('sign-up/<int:shift_id>/', views.sign_up, name='sign_up'),  # URL for signing up
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/drop-shift/<int:shift_id>/', views.drop_shift, name='drop_shift'),
    path('sign-up/', views.volunteer_sign_up, name='volunteer_sign_up'),
]