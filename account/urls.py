from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "account"


urlpatterns = [
    path("register/", views.register, name="register"),
    path("detail/", views.profile_detail, name="profile-detail"),
    path("delete/", views.profile_delete, name="profile-delete"),
    path("password-change/", auth_views.PasswordChangeView.as_view(), name="password-change"),
    path("password-change/done", auth_views.PasswordChangeDoneView.as_view(), name="password-change-done"),
]
