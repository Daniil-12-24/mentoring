from django.shortcuts import render
from .models import users

def index(request):
    greeting_text = 'Hello User!'

    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            user_instance, created = users.objects.get_or_create(u_name=name)
            if not created:
                # Если пользователь уже существует, увеличиваем press_count на 1
                user_instance.press_count += 1
            else:
                # Если это новый пользователь, устанавливаем press_count в 1
                user_instance.press_count = 1
            user_instance.save()

            greeting_text = f'Hello {name}!'

    data = users.objects.all()
    return render(request, 'main/index.html', {'data': data, 'greeting_text': greeting_text})

def count(request):
    data = users.objects.all()
    return render(request, 'main/count.html', {'data': data})
