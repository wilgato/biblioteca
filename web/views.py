from django.shortcuts import render, redirect
from .forms import aluno_form, livro_form, biblioteca_form
from .models import Alunos, Livros, Biblioteca

# Create your views here.

def cadastrar_aluno(request):
    if request.method == 'POST':
        form_aluno = aluno_form.AlunoForm(request.POST, request.FILES)
        if form_aluno.is_valid():
            form_aluno.save()
    else:
        form_aluno = aluno_form.AlunoForm()
    return render(request, 'form_aluno.html', {'form_aluno': form_aluno})

def cadastrar_livro(request):
    if request.method == 'POST':
        form_livro= livro_form.LivroForm(request.POST, request.FILES)
        if form_livro.is_valid():
            form_livro.save()
    else:
        form_livro = livro_form.LivroForm()
    return render(request, 'form_livro.html', {'form_livro': form_livro})

def cadastrar_biblioteca(request):
    if request.method == 'POST':
        form_biblioteca= biblioteca_form.BibliotecaForm(request.POST, request.FILES)
        if form_biblioteca.is_valid():
            form_biblioteca.save()
    else:
        form_biblioteca = biblioteca_form.BibliotecaForm()
    return render(request, 'form_biblioteca.html', {'form_biblioteca': form_biblioteca})


def listar_alunos(request):
    alunos = Alunos.objects.all()
    return render(request, 'lista_alunos.html', {'alunos': alunos})

def listar_livros(request):
    livros = Livros.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros})

def listar_bibliotecas(request):
    bibliotecas = Biblioteca.objects.all()
    return render(request, 'lista_bibliotecas.html', {'bibliotecas': bibliotecas})


def editar_aluno(request, aluno_id):
    aluno = Alunos.objects.get(id=aluno_id)
    if request.method == "POST":
        form_aluno = aluno_form.AlunoForm(request.POST or None, request.FILES, instance=aluno)
        if form_aluno.is_valid():
            form_aluno.save()
        return redirect('listar_alunos')
    else:
        form_aluno = aluno_form.AlunoForm(instance=aluno)
    return render(request, 'form_aluno.html', {'form_aluno': form_aluno})

def editar_livro(request, livro_id):
    livro = Livros.objects.get(id=livro_id)
    if request.method == "POST":
        form_livro = livro_form.LivroForm(request.POST or None, request.FILES, instance=livro)
        if form_livro.is_valid():
            form_livro.save()
        return redirect('listar_livros')
    else:
        form_livro = livro_form.LivroForm(instance=livro)
    return render(request, 'form_livro.html', {'form_livro': form_livro})

def editar_biblioteca(request, biblioteca_id):
    biblioteca = Biblioteca.objects.get(id=biblioteca_id)
    if request.method == "POST":
        form_biblioteca = form_biblioteca.BibliotecaForm(request.POST or None, request.FILES, instance=biblioteca)
        if form_biblioteca.is_valid():
            form_biblioteca.save()
        return redirect('listar_bibliotecas')
    else:
        form_biblioteca = biblioteca_form.BibliotecaForm(instance=biblioteca)
    return render(request, 'form_biblioteca.html', {'form_biblioteca': form_biblioteca})


def remover_aluno(request, aluno_id):
    aluno = Alunos.objects.get(id=aluno_id)
    aluno.delete()
    return redirect('listar_alunos')

def remover_livro(request, livro_id):
    livro = Livros.objects.get(id=livro_id)
    livro.delete()
    return redirect('listar_livros')


def remover_biblioteca(request, biblioteca_id):
    biblioteca = Biblioteca.objects.get(id=biblioteca_id)
    biblioteca.delete()
    return redirect('listar_bibliotecas')

