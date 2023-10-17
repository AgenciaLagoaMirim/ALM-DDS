from django.urls import path

from .views import (
    UserCreateView,
    UserLoginView,
    UserLogoutView,
    UserPasswordResetCompleteView,
    UserPasswordResetConfirmView,
    UserPasswordResetDoneView,
    UserPasswordResetView,
    UserPasswordUpdateDoneView,
    UserPasswordUpdateView,
    UserUpdateView,
)

urlpatterns = [
    path("create/", UserCreateView.as_view(), name="create_user"),
    path("update/<int:pk>/", UserUpdateView.as_view(), name="update_user"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("password_update/", UserPasswordUpdateView.as_view(), name="password_update"),
    path(
        "password_update_done/",
        UserPasswordUpdateDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", UserPasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset_done/",
        UserPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        UserPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete/",
        UserPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
