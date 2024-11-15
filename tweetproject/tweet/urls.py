from . import views
from django.urls import path , include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('admin/', admin.site.urls),  # Uncomment if you need admin access
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('<int:tweet_id>/', views.tweet_detail, name='tweet_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]
