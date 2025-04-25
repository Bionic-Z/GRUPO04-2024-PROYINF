from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from users.views import SignUpView, dashboard_view, manage_users, update_user_roles, profile_view, edit_user_role

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('users/', manage_users, name='manage_users'),
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('usuarios/', manage_users, name='manage_users'),
    path('usuarios/update_roles/', update_user_roles, name='update_user_roles'),
    path('profile/', profile_view, name='profile'),
    path('usuarios/<int:pk>/edit-role/', edit_user_role, name='edit_user_role'),
]
