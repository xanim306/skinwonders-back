from django.urls import path,include
from .import views


app_name = 'accounts-api'

urlpatterns = [
    path('login/',views.LoginView.as_view(),name='login'),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("activate/<uuid>/", views.ActivationView.as_view(), name="activation"),
    path('reset/password/', views.ResetPasswordView.as_view(), name='reset_password'),
    path('reset/password/complete/<slug>/', views.ResetPasswordCompleteView.as_view(), name='reset_password_complete'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('profile/update/',views.ProfileUpdateView.as_view(),name='profile-update'),
    path('profile/password/change/',views.PasswordChangeView.as_view(),name='password-change'),

]
