from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('users/<int:pk>/', views.users_detail, name='users_detail'),
    path('users/<int:pk>/edit/', views.users_edit, name='users_edit'),
    path('files/new/', views.files_new, name="files_new"),
    path('files/<int:pk>/', views.files_detail, name="files_detail"),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
]