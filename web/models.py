from django.db import models

# Create your models here.
class Alunos(models.Model):
    nome_aluno=models.CharField(max_length=100, null=False, blank=False)
    cpf=models.CharField(max_length=11, null=False, blank=False, unique=True)
    telefone=models.CharField(max_length=11, null=False, blank=False)
    email=models.EmailField(null=False, blank=False, unique=True)
    logradouro=models.CharField(max_length=60, null=False, blank=False)
    numero=models.IntegerField(null=False, blank=False)
    bairro=models.CharField(max_length=30, null=False, blank=False)
    complemento=models.CharField(max_length=30, null=False, blank=True)
    cep=models.CharField(max_length=8, null=False, blank=False)
    estado=models.CharField(max_length=2, null=False, blank=False)
    foto_usuario=models.ImageField(null=False)

class Livros(models.Model):
    nome_livro=models.CharField(max_length=100, null=False, blank=False)
    nome_autor=models.CharField(max_length=100, null=False, blank=False)
    data_Entrada=models.DateField(null=False)
    foto_livro=models.ImageField(null=False)

class Biblioteca(models.Model):
    data_Entrada=models.DateField(null=False)
    data_Saida = models.DateField(null=False)
    codigo_ibge = models.ImageField(null=False, blank=False)
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    foto_livro=models.ImageField(null=False)
