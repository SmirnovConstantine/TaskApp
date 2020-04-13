from django.urls import path, include

from .views import create_view, delete_view, list_view, update_view, list_view_for_user, task_run_view

app_name = 'tasks'

urlpatterns = [
	path('create/', create_view, name='task_create'),
	path('list/', list_view, name='tasks_list'),
	path('<int:pk>/delete/', delete_view, name='task_delete'),
	path('<int:pk>/update/', update_view, name='task_update'),
	path('<int:user>/my_list/', list_view_for_user, name='list_view_for_user'),
	path('my_task/<int:pk>/run', task_run_view, name='run_task')
]