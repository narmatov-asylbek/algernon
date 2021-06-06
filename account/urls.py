from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    path('my-page/', views.UserProfileUpdateView.as_view(), name='profile'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('registration/', views.UserRegistrationView.as_view(), name='register'),

    path('change-settings/', views.update_user_settings, name='update_settings'),
    path('change-contacts/', views.update_user_contacts, name='update_contacts'),
]
