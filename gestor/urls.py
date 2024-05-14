"""
URL configuration for gestorBiblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('cad_livros/', views.cad_livros, name='cad_livros' ),
    path('livros/', views.livros_view, name='livros'),
    path('del_livro/<pk>', views.del_livro, name='del_livro'),
    path('upd_livro/<pk>', views.upd_livro, name='upd_livro'),
    
    path('login_user/', views.login_user, name='login_user' ),
    path('cad_user/', views.cad_user, name='cad_user' ),
    path('cad_user_admin/', views.cad_user_admin, name='cad_user_admin' ),
    path('usuarios/', views.user_view, name='usuarios'),
    path('del_user/<pk>', views.del_user, name='del_user' ),
    path('block_user/<pk>', views.block_user, name='block_user' ),
    path('desblock_user/<pk>', views.desblock_user, name='desblock_user' ),
    path('upd_user/<pk>', views.upd_user, name='upd_user'),
    path('logout/',views.LogoutPage,name='logout'),
    path('erro-permissao/', views.erro_permissao, name='erro_permissao'),
    path('meus_dados/', views.meus_dados, name='meus_dados'),


    path('adicionar_carrinho/<pk>', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('remover_carrinho/<pk>', views.remover_carrinho, name='remover_carrinho'),
    path('reservas/', views.reservas, name='reservas'),
    path('confirmacao_reserva/', views.confirmacao_reserva, name='confirmacao_reserva'),
    path('finalizar_reserva/', views.finalizar_reserva, name='finalizar_reserva'),
    path('upd_reserva/<pk>', views.upd_reserva, name='upd_reserva'),
    path('detalhes_reserva/<pk>', views.detalhes_reserva, name='detalhes_reserva'),
    path('detalhes_livro/<pk>', views.detalhes_livro, name='detalhes_livro'),
    path('upd_biblioteca/', views.upd_biblioteca, name='upd_biblioteca'),
    path('dados_biblioteca/', views.dados_biblioteca, name='dados_biblioteca'),
    # path('cad_user_adm/', views.dados_biblioteca, name='dados_biblioteca'),

    
]


handler403 = 'gestor.views.erro_permissao'

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)