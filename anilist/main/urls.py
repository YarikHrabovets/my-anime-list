from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/signup/', views.RegisterUserView.as_view(), name='signup'),
    path('accounts/login/', views.AuthoriseUserView.as_view(), name='login'),
    path('accounts/logout/', views.logout_user, name='logout'),
    path('accounts/my-profile/', views.PersonalProfileView.as_view(), name='personal_profile'),
    path('profiles/<slug:slug>', views.ProfileView.as_view(), name='profile'),
]
