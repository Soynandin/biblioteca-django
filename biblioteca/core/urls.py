from django.urls import path
from .views import HomeView, LivroList, LivroDetail, CategoriaList, CategoriaDetail, AutorList, AutorDetail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('livros/', LivroList.as_view(), name='livros-list'),
    path('livros/<int:pk>/', LivroDetail.as_view(), name='livro-detail'),
    path('categorias/', CategoriaList.as_view(), name='categorias-list'),
    path('categorias/<int:pk>/', CategoriaDetail.as_view(), name='categoria-detail'),
    path('autores/', AutorList.as_view(), name='autores-list'),
    path('autores/<int:pk>/', AutorDetail.as_view(), name='autor-detail'),
]
