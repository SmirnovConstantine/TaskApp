from django.urls import path, include

from .views import registerPage, loginPage, logoutUser, homePage

app_name = 'accounts'

urlpatterns = [
	path('', homePage, name='home'),
	path('login/', loginPage, name='login'),
	path('register/', registerPage, name='register'),
	path('logout/', logoutUser, name='logout')
]