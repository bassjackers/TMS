from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from .forms import CreateAccountForm, LoginForm
from .models import Account


class IndexView(TemplateView):
    template_name = 'home.html'
    succes_url = '/'


class CreateAccountView(FormView):
    template_name = 'register.html'
    form_class = CreateAccountForm
    success_url = '/'

    def form_valid(self, form):
        account = Account(
            email=form.data.get('email'),
            password=make_password(form.data.get('password')),
        )
        account.save()

        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')

        return super().form_valid(form)


def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/')


class ForgotPasswordView(FormView):
    template_name = 'forgot-password.html'
