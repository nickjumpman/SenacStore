from django.urls import path
from StoreApp import views


urlpatterns=[
    path('', views.index, name='index'),
    path('produtos/', views.produto_lista, name='produto_lista'),
    path('produto/<int:id>', views.produto_detalhe, name='produto_detalhe'),
    path('produtos/<int:id>', views.produto_lista_por_departamento, name='produto_lista_por_departamento'),
    path('sobre-a-empresa/', views.sobre_empresa, name='sobre-a-empresa'),
    path('cadastro/', views.cadastro, name= 'cadastro'),
    path('contato/', views.contato, name='contato')
]