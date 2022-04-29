from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

def cadastro(request):
    if request.method == "POST":
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        
        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')
        
        if password != password2:
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()

        print('Usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios\cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['senha']
        print(email, password)
        if (email or password) == '':
            print('Email e senha não podem estar vazios')
            return render(request, 'usuarios\login.html')
        else:
            if User.objects.filter(email=email).exists():
                nome = User.objects.filter(email=email).values_list('username', flat=True).get()
                user = auth.authenticate(request, username=nome, password=password)
                if user is not None:
                    auth.login(request, user)
                    messages.success(request, 'login realizado com sucesso.')
                    return redirect('dashboard')
                else:
                    return render(request, 'usuarios\login.html')
            else:
                return render(request, 'usuarios\login.html')

    else:
        return render(request, 'usuarios\login.html')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)

        dados = {
            'receitas': receitas
        }

        return render(request, 'usuarios\dashboard.html', dados)
    else:
        return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('index')

def criar_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)

        nova_receita = Receita.objects.create(pessoa=user, nome_receita=nome_receita, ingredientes=ingredientes, 
        modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria, foto_receita=foto_receita)

        nova_receita.save()

        return redirect('dashboard')
    else:
        return render(request, 'usuarios\criar_receita.html')
        