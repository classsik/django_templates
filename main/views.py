from django.shortcuts import render


def home(request):
    school = 'Елабужский политехнический колледж'
    group = '215-8'
    spec = '09.02.07 Информационные системы и программирование'
    prof = 'Программистом'

    return render(request, 'main/index.html', {'school': school, 'group': group, 'spec': spec, 'prof': prof})


def about(request):
    fio = 'Юлдашев Азат Ринатович'
    height = '100 см.'
    weight = '100 кг.'
    age = '100 лет.'

    return render(request, 'main/about.html', {'fio': fio, 'height': height, 'weight': weight, 'age': age})


def contacts(request):
    result = {
        'Телеграмм': '@classsink',
        'Вконтакте': '@classsink'
    }

    return render(request, 'main/contacts.html', {'contacts': result})
