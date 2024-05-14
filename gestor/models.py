from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .managers import CustomUserManager
from django.dispatch import receiver
from PIL import Image
import os
from django.utils import timezone

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    quantidade_disponivel = models.IntegerField(null=True)
    sinopse = models.TextField(max_length=300, null=True)
    foto = StdImageField('foto', upload_to="fotos", variations={'thumb': (124,124)}, default='', null=False)
 
    def __str__(self):
        return self.titulo
    
@receiver(models.signals.post_save, sender=Livro)
def redmensionar_img(sender,instance,**kwargs):
    if instance.foto:
        novo_tamanho = (300, 300)
        imagem = Image.open(instance.foto.path)
        imagem.thumbnail(novo_tamanho)
        imagem.save(instance.foto.path)

class CustomUser(AbstractUser):
    cpf = models.CharField(max_length=50,null=True, blank=False)
    telefone = models.CharField(max_length=50, null=True, blank=False)
    bloqueado = models.BooleanField(default=False, editable=False)
    admin = models.BooleanField(default=True, editable=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    

class Reserva(models.Model):
    livros = models.ManyToManyField(Livro)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_reserva = models.DateField(default=timezone.now)
    data_devolucao = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.usuario.username
    

class Biblioteca(models.Model):
    nome = models.CharField(max_length=50, null=True)
    endereco = models.CharField(max_length=1500, null=True)
    bairro = models.CharField(max_length=100,null=True)
    cidade = models.CharField(max_length=50,null=True)
    estado = models.CharField(max_length=50,null=True)
    telefone= models.CharField(max_length=50,null=True)
    cnpj= models.CharField(max_length=50,null=True)


    def __srt__(self):
        return self.nome

