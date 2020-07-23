from django.shortcuts import render
from webapp.models import Task, STATUS_CHOICES


def index_view(request):
    data = Task.objects.all()
    return render(request, 'index.html', context={
        'tasks': data
    })


def task_add_view(request):
    if request.method == "GET":
        return render(request, 'task_add.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        date = request.POST.get('date')
        task = Task.objects.create(description=description, status=status, date=date)
        context = {'task': task}
        return render(request, 'task_view.html', context)