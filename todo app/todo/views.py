from django.shortcuts import render , redirect
from django.http import HttpResponse

from .models import Todo
from .forms import TodoForm

# Create your views here.

def todo_list(request):
    todos = Todo.objects.order_by('due_date')
    # print(todos)  return list

    context = {
        'todos':todos
    }

    return render(request,'todo_list.html', context )


def todo_details(request, id):
    todo = Todo.objects.get(id=id)
    
    context = {
        'todo':todo
    }

    return render(request,'todo_list2.html', context)


def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")

    context = {
        'form':form
    }    

    return render(request,'todo_create.html', context)


def todo_updated(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
    
    context = {'form':form}
    return render(request,'todo_update.html', context)


def todo_delete(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')