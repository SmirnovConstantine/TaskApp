from django import forms

from .models import Tasks

class TaskModelForm(forms.ModelForm):
	class Meta:
		model = Tasks
		fields = ['user', 'title', 'need_hours', 'comments']

class TaskCloseForm(forms.ModelForm):
	class Meta:
		model = Tasks
		fields = ['closed',]
