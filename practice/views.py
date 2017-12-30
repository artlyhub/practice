from django.shortcuts import render

from .models import ToDoList

def todo_list(request):
    context = {'todo': ToDoList.objects.all()}
    return render(request, 'index.html', context)
