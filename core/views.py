# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView


class HomeView(SuccessMessageMixin, TemplateView):
    template_name = "core/index.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """
        É chamado antes de qualquer outro método de visualização ser executado e é
        responsável por processar a solicitação antes de renderizar o template ou
        executar a lógica.
        O método dispatch verificará se o usuário está autenticado usando o decorator
        @login_required.
        Se o usuário estiver autenticado, a visualização prosseguirá e
        renderizará o template "home.html" mostrando a lista de posts mais recentes.
        Caso o usuário não esteja autenticado, ele será redirecionado para a página de
        login antes de acessar a página inicial.
        """
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Utilizado para adicionar dados personalizados ao contexto do template antes
        que o template seja renderizado.
        Adiciona o objeto de usuário autenticado ao contexto com a chave "user",
        para que este objeto possa ser utilizado no template e exibir informações
        especifícas do usuário.
        """
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context
