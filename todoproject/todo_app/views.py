from django.shortcuts import render
from todo_app.models import ToDoList, ToDoItem
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    # Query to get all the ToDoList Objects in Database
    all_list = ToDoList.objects.all()
    all_items = ToDoItem.objects.all()

    # A dictionary that will contain the information we got
    context = {
        'all_list' : all_list,
        'all_items' : all_items
    }

    return render(request, 'todo_template.html', context)

class TaskCreate(CreateView):
    model = ToDoItem
    fields = '__all__'
    template_name = 'todo_create.html'
    success_url = reverse_lazy('tasks')






