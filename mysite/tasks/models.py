#/*-----------------------------------------------------*/
#//   													*/
#//	created by | Constantine Smirniov					*/
#//														*/
#//														*/
#//														*/
#//                                                     */ 
#//                                                     */ 
#/*-----------------------------------------------------*/

from django.db import models
from django.conf import settings

# Модели заданий содержит, 
#  1 - user -> ссылка на пользователя, который выполняет задачу
#  2 - title -> название задачи
#  3 - creationdate -> дату и время создания задачи
#  4 - datetime_start -> дату и время начала выполнения задачи
#  5 - datetime_end -> дата и время окончания выполнения задачи
#  6 - need_hours -> количество часов требуемых для решения задачи
#  7 - spent_hours -> количество часов фактически потраченых на решение задачи
#  8 - in_time -> выполнена ли задача в срок
#  9 - comments -> комментарии к задачи

class Tasks(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
	title = models.CharField(max_length=500, null=True, blank=True, verbose_name="Заголовок")
	creationdate = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
	datetime_start = models.DateTimeField(null=True, blank=True, verbose_name="Время начала")
	datetime_end = models.DateTimeField(null=True, blank=True, verbose_name="Время окончания")
	need_hours = models.FloatField(null=True, blank=True, verbose_name="Необходимое время")
	spent_hours = models.IntegerField(null=True, blank=True, verbose_name="Затраченое время")
	in_time = models.BooleanField(default=False, verbose_name="Во время?")
	comments = models.TextField(null=True, blank=True, verbose_name="Комментарии")
	closed = models.BooleanField(null=True, blank=True, verbose_name="Закрыта ли задача")
	
	class Meta:
		verbose_name = "Задание"
		verbose_name_plural = "Задания"

	def __str__(self):
		return self.title

	def get_delete_url(self):
		return "/tasks/{}/delete".format(self.pk)

	def get_update_url(self):
		return "/tasks/{}/update".format(self.pk)

	def get_run_url(self):
		return "/tasks/my_task/{}/run".format(self.pk)
