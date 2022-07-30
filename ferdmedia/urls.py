from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
   #path('login/', views.user_login, name='login'),
   path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
   path('', views.dashboard, name='dashboard'),
   
   ## Password change urls ##
   path('passwordChange/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
   path('passwordChangeDone/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='passwordChangeDone'),
   
   ## password reset urls ##
   path('passwordReset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
   path('passwordReset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
   path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
   
   ## Registration url ##
   path('register/', views.register, name='register'),
   path('edit/', views.edit, name="edit"),
  ]