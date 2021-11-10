from django.urls import path
from .views import cadastrar_aluno, cadastrar_livro, cadastrar_biblioteca, listar_alunos, listar_livros, listar_bibliotecas, editar_aluno, editar_livro, \
    editar_biblioteca, remover_aluno, remover_livro, remover_biblioteca

urlpatterns = [
    path('cadastrar_aluno', cadastrar_aluno, name='cadastrar_aluno'),
    path('cadastrar_livro', cadastrar_livro, name='cadastrar_livro'),
    path('cadastrar_biblioteca', cadastrar_biblioteca, name='cadastrar_biblioteca'),
    path('listar_alunos', listar_alunos, name='listar_alunos'),
    path('listar_livros', listar_livros, name='listar_livros'),
    path('listar_bibliotecas', listar_bibliotecas, name='listar_bibliotecas'),
    path('editar_aluno/<int:aluno_id>', editar_aluno, name='editar_aluno'),
    path('editar_livro/<int:livro_id>', editar_livro, name='editar_livro'),
    path('editar_biblioteca/<int:biblioteca_id>', editar_biblioteca, name='editar_biblioteca'),
    path('remover_aluno/<int:aluno_id>', remover_aluno, name='remover_aluno'),
    path('remover_livro/<int:livro_id>', remover_livro, name='remover_livro'),
    path('remover_biblioteca/<int:biblioteca_id>', remover_biblioteca, name='remover_biblioteca')
]