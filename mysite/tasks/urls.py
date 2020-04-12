from django.urls import path, include

from .views import create_view, delete_view, list_view

app_name = 'tasks'

urlpatterns = [
	path('create/', create_view, name='task_create'),
	path('list/', list_view, name='tasks_list'),
	path('<int:pk>/delete/', delete_view, name='task_delete'),
]