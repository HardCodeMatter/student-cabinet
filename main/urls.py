from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/create/', views.profile_create, name='profile_create'),
    path('profile/update/', views.profile_update, name='profile_update'),
]
