from django.shortcuts import render, redirect
from .models import users, user_data
from django.contrib.sessions.models import Session
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

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
            request.session['user_id'] = user.id
            request.session['user_login'] = login
            return redirect('index')
        except user_data.DoesNotExist:
            return render(request, 'main/login.html', {'error_message': 'Username or password - invalid!'})

    return render(request, 'main/login.html')

def logout(request):
    session_key = request.session.session_key

    if session_key:
        try:
            session = Session.objects.get(pk=session_key)
            session.delete()
        except Session.DoesNotExist:
            pass
    
    return redirect('index')
    

def signin(request):
    if request.method == 'POST':
        login = request.POST.get('user-login')
        password = request.POST.get('user-password')
        email = request.POST.get('user-email')
        count = request.POST.get('user-count')

        try:
            user_data.objects.get(u_email=email)
            messages.error(request, 'User with this email already exists!')
            return redirect('signin')
        except ObjectDoesNotExist:
            user = user_data(login=login, u_password=password, u_email=email, press_count=count)
            user.save()

            main_user = users(u_name=login, press_count=count)
            main_user.save()
            
            return redirect('my_account', user_id=user.id, user_login=login)

    return render(request, 'main/signin.html')

def my_account(request, user_id, user_login):
    user_id = request.session.get('user_id')
    user_login = request.session.get('user_login')

    if user_id and user_login:
        user = user_data.objects.get(id=user_id)
        return render(request, 'main/my_account.html', {'user': user, 'user_login': user_login})
    else:
        return redirect('login')

def edit_profile(request, user_id, user_login):
    if request.method == 'POST':
        new_email = request.POST.get('new-email')
        new_count = request.POST.get('new-count')
        new_login = request.POST.get('new-login')
        new_password = request.POST.get('new-password')

        user = user_data.objects.get(id=user_id)
        user.u_email = new_email
        user.press_count = new_count
        user.login = new_login
        user.u_password = new_password
        user.save()

        main_user = users.objects.get(u_name=user_login)
        main_user.press_count = new_count
        main_user.u_name = new_login
        main_user.save()

        request.session['user_login'] = new_login

        return redirect('my_account', user_id=user.id, user_login=new_login)


    
    user = user_data.objects.get(id=user_id)
    return render(request, 'main/edit_profile.html', {'user': user, 'user_login': user_login})