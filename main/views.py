from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, FilterForm


def index(request):                   #Переход на определенный индексацию.
    if request.method == 'POST':      #Пользователь отправляет данные нам используется GET.
        tasks = Task.objects.get(title__contains='')
    tasks = Task.objects.order_by('id')
    form = FilterForm()
    return render(request, 'main/index.html', {'title': 'Главная',    # Используется шаблонизатор Jinja в файле base, {% block title %}[% endblock %}
                                               'tasks': tasks,
                                               'form': form})   #Всё это = контекст запроса или же контекст. Передаем название страницы.


def create(request):
    error = ''
    if request.method == 'POST':  #Пользовватель отправляет данные на создание записи.
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  #После создание записи переадресация на главную.
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
