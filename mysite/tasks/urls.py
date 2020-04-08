from django.urls import path, include

from .views import create_view

app_name = 'tasks'

urlpatterns = [
	path('create/', create_view, name='task_create'),
]