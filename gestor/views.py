from django.shortcuts import render,HttpResponse,redirect
from . models import Livro, CustomUser, Reserva, Biblioteca
from .forms import LivrosForm, UserForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from django.contrib.auth.models import User,Group
from django.utils import timezone
from datetime import timedelta
from django.db import transaction


def index(request):
    livros = Livro.objects.order_by('titulo')
    user_is_admin = False  # Inicializa com um valor padrão
    user_is_block = False  # Inicializa com um valor padrão
    logado = request.user.is_authenticated
    biblioteca = Biblioteca.objects.get(id=1)

    if logado:
        if hasattr(request.user, 'admin'):
            user_is_admin = request.user.admin
        
        if hasattr(request.user, 'bloqueado'):
            user_is_block = request.user.bloqueado
    
    carrinho = request.session.get('carrinho', {})

    context = {'livros': livros, 'user_is_admin': user_is_admin, 'user_is_block': user_is_block, 'logado': logado, 'carrinho' : carrinho, 'biblioteca':biblioteca}
    return render(request, "index.html", context)



@login_required
def livros_view(request):
    livros = Livro.objects.order_by('titulo')

    user_is_admin = False  # Inicializa com um valor padrão
    user_is_block = False  # Inicializa com um valor padrão
    logado = request.user.is_authenticated

    if logado:
        if hasattr(request.user, 'admin'):
            user_is_admin = request.user.admin
        
        if hasattr(request.user, 'bloqueado'):
            user_is_block = request.user.bloqueado
    
    context = {'livros': livros, 'user_is_admin': user_is_admin, 'user_is_block': user_is_block, 'logado': logado}
    return render(request, 'pages/livros.html', context)

@login_required
def cad_livros(request):
    if request.method != 'POST':
        form = LivrosForm()
    else:
        form = LivrosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('livros'))
    context = {'form':form}
    return render(request, 'pages/cad_livros.html', context)

@login_required
def upd_livro(request,pk):
    update = Livro.objects.get(id=pk)

    if( request.method != 'POST' ):
        form = LivrosForm(instance=update)
    else:
        form = LivrosForm(instance=update, data=request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse('livros'))
    context = {'update' : update ,'pk' : pk , 'form' : form}
    return render(request, 'pages/upd_livro.html', context)

@login_required
def del_livro(request, pk):
    deletar = Livro.objects.get(id=pk)
    if(request.method == 'POST'):
        deletar.delete()
        return HttpResponseRedirect(reverse('livros'))
    context = {'deletar': deletar, 'pk' : pk}
    return render(request, 'pages/del_livro.html', context)

def detalhes_livro(request,pk):
    livro = Livro.objects.get(id=pk)
    context = {'livro':livro}
    return render(request, 'pages/detalhes_livro.html', context)




def user_view(request):
    usuarios = CustomUser.objects.all()
    user_is_admin = False  # Inicializa com um valor padrão
    user_is_block = False  # Inicializa com um valor padrão
    logado = request.user.is_authenticated

    if logado:
        if hasattr(request.user, 'admin'):
            user_is_admin = request.user.admin
        
        if hasattr(request.user, 'bloqueado'):
            user_is_block = request.user.bloqueado
    
    context = {'usuarios': usuarios, 'user_is_admin': user_is_admin, 'user_is_block': user_is_block, 'logado': logado}
    return render(request, 'pages/usuarios.html', context)




def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'pages/login_user.html')



def cad_user(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        cpf=request.POST.get("cpf")
        telefone=request.POST.get("telefone")
        
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            bloqueado = False
            admin = False
            
            my_user=CustomUser.objects.create_user(uname,email,pass1,cpf,telefone,admin,bloqueado)
            my_user.save()
            return redirect('login_user')
    
    return render(request, 'pages/cad_user.html')
        
def cad_user_admin(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        cpf=request.POST.get("cpf")
        telefone=request.POST.get("telefone")
        admin = request.POST.get('admin')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            bloqueado = False
            
            my_user=CustomUser.objects.create_user(uname,email,pass1,cpf,telefone,admin,bloqueado)
            my_user.save()
            return redirect('usuarios')
    
    return render(request, 'pages/cad_user_admin.html')


def LogoutPage(request):
    logout(request)
    return redirect('index')

def upd_user(request,pk):
    update = CustomUser.objects.get(id=pk)

    if( request.method == 'POST' ):
        update.username =request.POST.get('username')
        update.email=request.POST.get('email')
        update.set_password(request.POST.get('password1'))
        update.cpf=request.POST.get("cpf")
        update.telefone=request.POST.get("telefone")
        update.save()

        return HttpResponseRedirect(reverse('meus_dados'))
    context = {'update' : update ,'pk' : pk}
    return render(request, 'pages/upd_user.html', context)

def block_user(request,pk):
    update = CustomUser.objects.get(id=pk)

    if( request.method == 'POST' ):
        update.bloqueado=True
        update.save()

        return HttpResponseRedirect(reverse('usuarios'))
    context = {'update' : update ,'pk' : pk}
    return render(request, 'pages/block_user.html', context)

def desblock_user(request,pk):
    update = CustomUser.objects.get(id=pk)

    if( request.method == 'POST' ):
        update.bloqueado=False
        update.save()

        return HttpResponseRedirect(reverse('usuarios'))
    context = {'update' : update ,'pk' : pk}
    return render(request, 'pages/desblock_user.html', context)


def del_user(request, pk):
    deletar = CustomUser.objects.get(id=pk)
    if(request.method == 'POST'):
        deletar.delete()
        return HttpResponseRedirect(reverse('usuarios'))
    context = {'deletar': deletar, 'pk' : pk}
    return render(request, 'pages/del_user.html', context)

def erro_permissao(request, exception=permission_required):
    return render(request, 'pages/acesso_negado.html', status=403)


def meus_dados(request):
    user_is_admin = False  # Inicializa com um valor padrão
    user_is_block = False  # Inicializa com um valor padrão
    logado = request.user.is_authenticated
    if logado:
        if hasattr(request.user, 'admin'):
            user_is_admin = request.user.admin
        
        if hasattr(request.user, 'bloqueado'):
            user_is_block = request.user.bloqueado
    
    context = {'user_is_admin': user_is_admin, 'user_is_block': user_is_block, 'logado': logado}
    return render(request, 'pages/meus_dados.html', context)


def adicionar_carrinho(request, pk):
    livro = Livro.objects.get(id=pk)
    
    
    carrinho = request.session.get('carrinho', {})  # Obtém o carrinho da sessão ou um dicionário vazio
    carrinho[pk] = {
        'id': pk,
        'titulo': livro.titulo,
        'autor': livro.autor,
    }
    print(carrinho[pk]['titulo'])
    print("adicionado")

    request.session['carrinho'] = carrinho  # Atualiza o carrinho na sessão

    return redirect('index')

def remover_carrinho(request, pk):
    if 'carrinho' in request.session and pk in request.session['carrinho']:
        del request.session['carrinho'][pk]
        request.session.modified = True
    return redirect('confirmacao_reserva')

def finalizar_reserva(request):
    if request.method == 'POST':
        # Verifica se o usuário está autenticado
        if request.user.is_authenticated:
            carrinho = request.session.get('carrinho', {})
            if carrinho == {}:
                return HttpResponse("Carrinho esta vazio!")
            if request.POST.get('user'):
                usuarioReserva = CustomUser.objects.get(id=request.POST.get('user'))
            else: 
                usuarioReserva = request.user
            if carrinho:
                with transaction.atomic():
                    reserva = Reserva.objects.create(
                        usuario=usuarioReserva,
                        data_reserva=timezone.now(),
                        data_devolucao=timezone.now() + timedelta(days=7),
                        status="reservado"
                    )
                    for livro_id, quantidade in carrinho.items():
                        livro = Livro.objects.get(pk=livro_id)
                        reserva.livros.add(livro)
                    
                    request.session['carrinho'] = {}
                    messages.success(request, "Reserva finalizada com sucesso!")
                    return redirect('reservas')
            else:
                messages.warning(request, "Carrinho vazio! Adicione livros ao carrinho para finalizar a reserva.")
                return redirect('index')
        else:
            messages.warning(request, "Você precisa estar logado para finalizar a reserva.")
            return redirect('login_user')  # ou qualquer outra página de login
    else:
        messages.error(request, "Método não permitido.")
        return redirect('index')  # ou qualq
    

def reservas(request):
    user_is_admin = False  # Inicializa com um valor padrão
    user_is_block = False  # Inicializa com um valor padrão
    logado = request.user.is_authenticated
    if logado:
        if hasattr(request.user, 'admin'):
            user_is_admin = request.user.admin
        
        if hasattr(request.user, 'bloqueado'):
            user_is_block = request.user.bloqueado
    
    if user_is_admin :
        reservas = Reserva.objects.all()
    else:
        reservas = Reserva.objects.filter(usuario_id=request.user.id)
    
    context = {'reservas': reservas, 'user_is_admin': user_is_admin, 'user_is_block': user_is_block, 'logado': logado}
    return render(request, "pages/reservas.html", context)

def confirmacao_reserva(request):
    carrinho = request.session.get('carrinho', {})

    user_is_admin = False  # Inicializa com um valor padrão
    logado = request.user.is_authenticated
    if logado:
        if hasattr(request.user, 'admin'):
            user_is_admin = request.user.admin
        
    
    if user_is_admin :
        usuarios = CustomUser.objects.all()
    else:
        usuarios = None

    context = {'carrinho': carrinho, 'usuarios':usuarios, 'user_is_admin':user_is_admin}
    return render(request, "pages/confirmacao_reserva.html", context)


def upd_reserva(request,pk):
    update = Reserva.objects.get(id=pk)

    if( request.method == 'POST' ):
        livros = update.livros.all()
        update.status = "devolvido"
        update.save()

        for livro in livros:
            livro.quantidade_disponivel = livro.quantidade_disponivel +1
            livro.save()

        return HttpResponseRedirect(reverse('reservas'))
    context = {'update' : update ,'pk' : pk}
    return render(request, 'pages/upd_reserva.html', context)

def detalhes_reserva(request,pk):
    reserva = Reserva.objects.get(id=pk)
    livros_reserva = reserva.livros.all()    
    context = {'reserva' : reserva, 'livros':livros_reserva}
    return render(request, 'pages/detalhes_reserva.html', context)


def dados_biblioteca(request):
    user_is_admin = False  # Inicializa com um valor padrão
    user_is_block = False  # Inicializa com um valor padrão
    logado = request.user.is_authenticated
    biblioteca = Biblioteca.objects.get(id=1)

    if logado:
        if hasattr(request.user, 'admin'):
            user_is_admin = request.user.admin
        
        if hasattr(request.user, 'bloqueado'):
            user_is_block = request.user.bloqueado
    
    context = {'user_is_admin': user_is_admin, 'user_is_block': user_is_block, 'logado': logado, 'biblioteca':biblioteca}
    return render(request, 'pages/dados_biblioteca.html', context)

def upd_biblioteca(request):
    user_is_admin = False  # Inicializa com um valor padrão
    user_is_block = False  # Inicializa com um valor padrão
    logado = request.user.is_authenticated
    if logado:
        if hasattr(request.user, 'admin'):
            user_is_admin = request.user.admin
        
        if hasattr(request.user, 'bloqueado'):
            user_is_block = request.user.bloqueado

    

    update = Biblioteca.objects.get(id=1)
    if request.method=='POST':
        update.nome=request.POST.get('nome')
        update.endereco=request.POST.get('endereco')
        update.cidade=request.POST.get('cidade')
        update.bairro=request.POST.get('bairro')
        update.estado=request.POST.get("estado")
        update.telefone=request.POST.get("telefone")
        update.cnpj=request.POST.get("cnpj")
        update.save()
        

        return HttpResponseRedirect(reverse('dados_biblioteca'))  
    
    context = {'user_is_admin': user_is_admin, 'user_is_block': user_is_block, 'logado': logado}
    return render(request, 'pages/upd_biblioteca.html', context)