from django.contrib import admin
from django.urls import path
from acervo.views import listar_pecas, cadastrar_peca
from visitantes.views import listar_visitantes, registrar_visitante
from exposicoes.views import listar_exposicoes, cadastrar_exposicao
from categorias.views import listar_categorias, cadastrar_categoria
from restauracoes.views import listar_restauracoes, registrar_restauracao
from usuarios.views import listar_usuarios, cadastrar_usuario

urlpatterns = [
    path('admin/', admin.site.urls),

    # Acervo (Home)
    path('', listar_pecas, name='listar_pecas'), 
    path('pecas/nova/', cadastrar_peca, name='cadastrar_peca'),

    # Categorias
    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/nova/', cadastrar_categoria, name='cadastrar_categoria'),

    # Visitantes
    path('visitantes/', listar_visitantes, name='listar_visitantes'),
    path('visitantes/novo/', registrar_visitante, name='registrar_visitante'),

    # Exposições
    path('exposicoes/', listar_exposicoes, name='listar_exposicoes'),
    path('exposicoes/nova/', cadastrar_exposicao, name='cadastrar_exposicao'),

    # Restaurações
    path('restauracoes/', listar_restauracoes, name='listar_restauracoes'),
    path('restauracoes/nova/', registrar_restauracao, name='registrar_restauracao'),

    # Usuários
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
    path('usuarios/novo/', cadastrar_usuario, name='cadastrar_usuario'),
]