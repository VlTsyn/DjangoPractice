from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import RegisterView, UserDetailView, UserUpdateView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:catalog'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_profile'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
]