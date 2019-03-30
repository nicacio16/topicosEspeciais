from django.shortcuts import render

from django.views.generic import TemplateView


# Create your views here.

# Cria uma classe com herança de TemplateView para exibir
# um arquivo HTML normal (com o conteúdo dele)
class PaginaInicialView(TemplateView):
    # Nome do arquivo que vai ser utilizado para renderizar
    # esta página/método/classe
    template_name = "index.html"

# Pagina de "Team"
class TeamView(TemplateView):
    template_name = "team.html"

# Pagina de "Contato"
class ContatoView(TemplateView):
    template_name = "contato.html"

# Página "Sobre"
class SobreView(TemplateView):
    template_name = "sobre.html"
