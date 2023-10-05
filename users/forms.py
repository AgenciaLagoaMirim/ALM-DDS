from typing import Any

from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
    UserChangeForm,
    UserCreationForm,
)
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class CustomUserCreateForm(UserCreationForm):
    password1 = forms.CharField(
        label="Senha", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    password2 = forms.CharField(
        label="Confirmar senha",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
        )
        help_texts = {"username": None}
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            # "is_active": forms.HiddenInput(attrs={"class": "form-control"}),
        }
        labels = {
            "email": "Email:",
            "username": "Nome de usuário:",
            "first_name": "Nome:",
            "last_name": "Sobrenome:",
            # "is_active": "Usuário ativo ?",
        }

    def clean_password2(self) -> str:
        """
        Verifica se as senhas fornecidas são identicas.
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValueError(_("Passwords don't match"))

        return password2

    def save(self, commit=True):
        """
        Salva o password fornecido criptografado em hash
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        print(_("Success in registering user!"))
        if commit:
            user.save()
        return user


class CustomUserUpdateForm(UserChangeForm):
    def __init__(self, user, *args: Any, **kwargs: Any) -> None:
        print(f"user type: {user.type_user}")
        super().__init__(*args, **kwargs)
        self.fields.pop("password")
        if user.type_user not in ["adm", "col"]:
            print("Campos removidos: is_active e type_user")
            del self.fields["is_active"]
            del self.fields["type_user"]

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "type_user",
            "is_active",
        )
        help_texts = {"username": None}
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-control"}),
        }
        labels = {
            "email": "Email:",
            "username": "Nome de usuário:",
            "first_name": "Nome:",
            "last_name": "Sobrenome:",
            "is_active": "Usuário ativo ?",
        }


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Email de usuário:",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "Insira um endereço de email.",
            "invalid": "Insira um formato de email válido: exemplo@email.com",
        },
    )
    password = forms.CharField(
        label="Senha:",
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "Insira uma senha.",
        },
    )


class CustomUserPasswordUpdateForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Senha atual", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    new_password1 = forms.CharField(
        label="Nova senha", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    new_password2 = forms.CharField(
        label="Confirmar nova senha",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )


class CustomUserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=("Digite seu email"),
        max_length=254,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "autocomplete": "email"}
        ),
    )


class CustomUserPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="Nova senha", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    new_password2 = forms.CharField(
        label="Confirmar nova senha",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
