from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import time

from .forms import CreateUserForm


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('accounts:register')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was crated for ' + user)

				return redirect('accounts:login')

		context = {'form': form}
		return render(request, 'accounts/register.html', context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				time.sleep(2)
				return redirect('/')
		else:
			messages.info(request, 'username OR password is inccorect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('accounts:login')

def homePage(request):
	context = {}
	return render(request, 'base.html', context)



	