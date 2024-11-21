from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),  # Uncomment if you need admin access
    path('', views.index, name='index'),  # Added index view
    path('tweet/', views.tweet_list, name='tweet_list'),
     path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('tweets/create/', views.tweet_create, name='tweet_create'),
    path('tweets/<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('tweets/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('tweets/<int:tweet_id>/', views.tweet_detail, name='tweet_detail'),
    path('accounts/', include('django.contrib.auth.urls')),  # Handles login, logout, password reset, etc.
    path('register/', views.register, name='register'),  # Added register view
]
