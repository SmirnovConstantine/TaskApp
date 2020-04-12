from django.shortcuts import render, redirect

from .forms import TaskModelForm
from .models import Tasks

def create_view(request):

	form = TaskModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('tasks:tasks_list')

	context = {
		'form': form,
	}

	return render(request, "tasks/task_create.html", context)

def list_view(request):
	tasks = Tasks.objects.all()
	context = {
		'objects_list': tasks,
	}

	return render(request, "tasks/list.html" ,context)

def delete_view(request, pk):
	item_to_delete = Tasks.objects.filter(pk=pk)
	if item_to_delete.exists():
		if request.user == item_to_delete[0].user:
			item_to_delete[0].delete() 
	return redirect('tasks:tasks_list')

