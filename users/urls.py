from django.urls import path
from django.contrib.auth import views as auth_views
from .views import LogoutView, RegisterView

urlpatterns = [
	path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	path('logout', LogoutView.as_view(), name='logout'),
	path('register', RegisterView.as_view(), name='register')
]

