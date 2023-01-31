from django.urls import path

from . import views

app_name = "account"


urlpatterns = [
    path("register/", views.register, name="register"),
    path("detail/", views.profile_detail, name="profile-detail"),
    path("delete/", views.profile_delete, name="profile-delete"),
]
