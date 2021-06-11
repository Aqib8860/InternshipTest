from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import authenticate, login, logout
from .forms import *


# Create your views here.


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    initial = {'key': 'value'}
    template_name = 'user_register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, 'Account was created for ' + email)
            return redirect('core:user-register')
        return render(request, self.template_name, {'form': form})


class LoginView(TemplateView):
    form_class = UserLoginForm
    initial = {'key': 'value'}
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
    	form = self.form_class(request.POST)
    	email = request.POST['email']
    	password = request.POST['password']
    	user = authenticate(request, email=email, password=password)
    	if user is not None:
    		login(request, user)
    		return redirect('core:user-home')
    	else:
    		messages.info(request, 'Username OR Password is Incorrect')
    	return render(request, self.template_name, {'form': form})


def userLogout(request):
    logout(request)
    return redirect('core:home')


class UserHomeView(TemplateView):
    template_name = 'user_home.html'
