from django.shortcuts import render
from webapp.models import Task, STATUS_CHOICES


def index_view(request):
    is_admin = request.GET.get('is_admin', None)
    if is_admin:
        data = Task.objects.all()
    else:
        data = Task.objects.filter(status='moderated')
    return render(request, 'index.html', context={
        'tasks': data
    })


def task_add_view(request):
    if request.method == "GET":
        return render(request, 'task_add.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        description = request.POST.get('title')
        status = request.POST.get('status')
        date = request.POST.get('status')
        task = Task.objects.create(description=description, status=status, date= date)
        context = {'article': task}
        return render(request, 'task_view.html', context)