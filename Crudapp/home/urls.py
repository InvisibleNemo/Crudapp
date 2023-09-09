# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='login'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),  # Ensure the name is 'dashboard'
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile'),  # Use ProfileDetailView for viewing
    path('profile/<int:pk>/edit/', views.ProfileUpdateView.as_view(), name='profile_edit'),  # Use ProfileUpdateView for editing

]
