from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    path('u/<slug:slug>/lib', views.AccountLibraryView.as_view(), name='library'),
    path('u/<slug:slug>/', views.ProfileInfoView.as_view(), name='profile'),
    path('my-page/', views.UserSettingsUpdateView.as_view(), name='settings'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('registration/', views.UserRegistrationView.as_view(), name='register'),

    path('change-settings/', views.update_user_settings, name='update_settings'),
    path('change-contacts/', views.update_user_contacts, name='update_contacts'),

    path('friends/send/<int:user_id>/', views.send_friend_request, name='send_friend_request'),
    path('friends/add/<int:request_id>/', views.accept_friend_request, name='accept_friends'),
    path('subscribers/', views.AccountSubscribersList.as_view(), name='subscriber_list')
]

