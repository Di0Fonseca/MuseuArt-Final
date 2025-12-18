from django.contrib import admin
from django.urls import path
from acervo.views import listar_pecas, cadastrar_peca
from visitantes.views import listar_visitantes, registrar_visitante
from exposicoes.views import listar_exposicoes, cadastrar_exposicao
from categorias.views import listar_categorias, cadastrar_categoria
from restauracoes.views import listar_restauracoes, registrar_restauracao
from usuarios.views import listar_usuarios, cadastrar_usuario
from acervo.views import listar_pecas, cadastrar_peca, index
from categorias.views import listar_categorias, cadastrar_categoria, editar_categoria, excluir_categoria


from django.conf import settings 
from django.conf.urls.static import static 

from acervo.views import listar_pecas, cadastrar_peca, index, editar_peca, excluir_peca
from restauracoes.views import listar_restauracoes, registrar_restauracao, editar_restauracao, excluir_restauracao
from exposicoes.views import listar_exposicoes, cadastrar_exposicao, editar_exposicao, excluir_exposicao
from visitantes.views import listar_visitantes, registrar_visitante, editar_visitante, excluir_visitante

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('acervo/', listar_pecas, name='listar_pecas'),
    
    # Acervo (Home)
    path('', listar_pecas, name='listar_pecas'), 
    path('pecas/nova/', cadastrar_peca, name='cadastrar_peca'),
    
    path('pecas/editar/<int:id>/', editar_peca, name='editar_peca'),
    path('pecas/excluir/<int:id>/', excluir_peca, name='excluir_peca'),
    
    # Categorias
    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/nova/', cadastrar_categoria, name='cadastrar_categoria'),
    path('categorias/editar/<int:id>/', editar_categoria, name='editar_categoria'),
    path('categorias/excluir/<int:id>/', excluir_categoria, name='excluir_categoria'),
    
    # Visitantes
    path('visitantes/', listar_visitantes, name='listar_visitantes'),
    path('visitantes/novo/', registrar_visitante, name='registrar_visitante'),
    
    path('visitantes/editar/<int:id>/', editar_visitante, name='editar_visitante'),
    path('visitantes/excluir/<int:id>/', excluir_visitante, name='excluir_visitante'),

    # Exposições
    path('exposicoes/', listar_exposicoes, name='listar_exposicoes'),
    path('exposicoes/nova/', cadastrar_exposicao, name='cadastrar_exposicao'),
    
    path('exposicoes/editar/<int:id>/', editar_exposicao, name='editar_exposicao'),
    path('exposicoes/excluir/<int:id>/', excluir_exposicao, name='excluir_exposicao'),

    # Restaurações
    path('restauracoes/', listar_restauracoes, name='listar_restauracoes'),
    path('restauracoes/nova/', registrar_restauracao, name='registrar_restauracao'),
    path('restauracoes/editar/<int:id>/', editar_restauracao, name='editar_restauracao'),
    path('restauracoes/excluir/<int:id>/', excluir_restauracao, name='excluir_restauracao'),

    # Usuários
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
    path('usuarios/novo/', cadastrar_usuario, name='cadastrar_usuario'),
    
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)