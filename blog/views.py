from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.
def index(request):
    todos_list = Todo.objects.all()
    todo_form = TodoForm(request.POST or None)
    if todo_form.is_valid():
        todo_form.save()
        todo_form = TodoForm()

    context = {
        "todos_list": todos_list,
        "form": todo_form
    }
    return render(request, 'home.html', context)


def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('home_view')