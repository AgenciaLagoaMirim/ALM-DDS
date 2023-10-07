from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView

from users.forms import (
    CustomUserCreateForm,
    CustomUserLoginForm,
    CustomUserPasswordResetConfirmForm,
    CustomUserPasswordResetForm,
    CustomUserPasswordUpdateForm,
    CustomUserUpdateForm,
)

from .models import CustomUser


def custom_404_view(request, exception):
    return render(request, "base/404.html", status=404)


def custom_403_view(request, exception):
    return render(request, "base/403.html", status=404)


class UserLoginView(LoginView):
    form_class = CustomUserLoginForm
    template_name = "users/registration/login.html"


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")


class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreateForm
    template_name = "users/registration/user_create.html"
    success_url = reverse_lazy("home")


class UserUpdateView(
    LoginRequiredMixin,
    UpdateView,
):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = "users/registration/user_update.html"
    success_url = reverse_lazy("home")

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.type_user == "adm":
            return queryset

        return queryset.filter(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        try:
            user_id = kwargs["pk"]
        except ObjectDoesNotExist:
            raise PermissionDenied("Object does not exist. Redirect to home.")

        if self.request.user.type_user == "adm" or self.request.user.id == user_id:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied("Object does not exist. Redirect to home.")

    def form_valid(self, form):
        form.save()  # Salva as alterações no perfil do usuário
        return super().form_valid(form)


class UserPasswordUpdateView(PasswordChangeView):
    form_class = CustomUserPasswordUpdateForm
    template_name = "users/registration/password_update.html"


class UserPasswordUpdateDoneView(PasswordChangeDoneView):
    template_name = "users/registration/password_update_done.html"

    def get_success_url(self):
        return reverse("password_update_done")


class UserPasswordResetView(PasswordResetView):
    form_class = CustomUserPasswordResetForm
    template_name = "users/registration/password_reset.html"


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = "users/registration/password_reset_done.html"


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomUserPasswordResetConfirmForm
    template_name = "users/registration/password_reset_confirm.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        # Adicione um log para verificar se esta função está sendo chamada
        print("Formulário de redefinição de senha válido")
        return response


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "users/registration/password_reset_complete.html"
