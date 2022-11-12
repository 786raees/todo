from django.shortcuts import render
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