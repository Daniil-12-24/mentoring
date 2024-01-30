from django.shortcuts import render, redirect
from .models import users, user_data

def index(request):
    greeting_text = 'Hello User!'

    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            user_data, created = users.objects.get_or_create(u_name=name)
            if not created:
                # Если пользователь уже существует, увеличиваем press_count на 1
                user_data.press_count += 1
            else:
                # Если это новый пользователь, устанавливаем press_count в 1
                user_data.press_count = 1
                
            user_data.save()

            greeting_text = f'Hello {name}!'

    data = users.objects.all()
    return render(request, 'main/index.html', {'data': data, 'greeting_text': greeting_text})

def count(request):
    data = users.objects.all()
    return render(request, 'main/count.html', {'data': data})

def login(request):
    if request.method == 'POST':
        login = request.POST.get('user-login')
        password = request.POST.get('user-password')

        try:
            user = user_data.objects.get(login=login, u_password=password)
            return render(request, 'main/login.html', {'message': 'Success!', 'username': user.login, 'count': user.press_count})
        except user_data.DoesNotExist:
            return render(request, 'main/login.html', {'error_message': 'Username or password - invalid!'})

    return render(request, 'main/login.html')

def signin(request):
    if request.method == 'POST':
        login = request.POST.get('user-login')
        password = request.POST.get('user-password')
        email = request.POST.get('user-email')
        count = request.POST.get('user-count')

        user = user_data(login=login, u_password=password, u_email=email, press_count=count)
        user.save()

        return redirect('greetings', user_name=login, user_count=count)

    return render(request, 'main/signin.html')

def greetings(request, user_name, user_count):
    return render(request, 'main/greetings.html', {'user_name': user_name, 'user_count': user_count})