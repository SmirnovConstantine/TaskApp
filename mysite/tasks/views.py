from django.shortcuts import render, redirect, get_object_or_404

from .forms import TaskModelForm, TaskCloseForm
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

def update_view(request, pk):

	item_to_update = get_object_or_404(Tasks, pk=pk)
	form = TaskModelForm(request.POST or None, instance=item_to_update)
	if form.is_valid():
		form.instance.user = request.user
		form.save()
		return redirect('tasks:tasks_list')

	context = {
		'form': form,
	}

	return render(request, 'tasks/task_create.html', context)

def list_view_for_user(request, user):
	item_for_user = Tasks.objects.filter(user=request.user)
	context = {
		'item_for_user': item_for_user, 
	}
	return render(request, 'tasks/list_for_user.html', context)

def task_run_view(request, pk):
	item_to_run = Tasks.objects.filter(pk=pk)
	context = {
		'item_to_run': item_to_run,
	}
	return render(request, 'tasks/run.html', context)

# TODO
def close_task(request, pk):
	item_to_close = get_object_or_404(Tasks, pk=pk)
	form = TaskCloseForm(request.POST or None, instance=item_to_close)
	if form.is_valid():
		form.instance.closed = True
		form.save()
	context = {
		'form': form,
	}
	return render(request, 'tasks/run.html', context)
