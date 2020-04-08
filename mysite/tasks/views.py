from django.shortcuts import render, redirect

from .forms import TaskModelForm
from .models import Tasks

def create_view(request):

	form = TaskModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/')

	context = {
		'form': form,
	}

	return render(request, "tasks/task_create.html", context)


