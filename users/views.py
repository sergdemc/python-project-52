from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import UserPermissionCheckMixin, LoginFlashMixin
from django.contrib.messages.views import SuccessMessageMixin

from users.models import User
from users.forms import RegisterUsersForm, LoginForm


class ListUsersView(ListView):
    model = User
    template_name = 'users/list_users.html'
    context_object_name = 'users'


class UpdateUsersView(SuccessMessageMixin, LoginFlashMixin, UserPermissionCheckMixin, UpdateView):
    model = User
    form_class = RegisterUsersForm
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('list_users')
    pk_url_kwarg = "user_id"
    login_url = reverse_lazy('login')
    success_message = "The user was updated successfully"


class DeleteUsersView(SuccessMessageMixin, LoginFlashMixin, UserPermissionCheckMixin, DeleteView):
    model = User
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy('list_users')
    pk_url_kwarg = "user_id"
    login_url = reverse_lazy('login')
    success_message = "The user was deleted successfully"


class RegisterUsersView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/user_create.html'
    form_class = RegisterUsersForm
    success_url = reverse_lazy('login')
    success_message = "The user was created successfully"


class LoginUserView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    next_page = '/'
    authentication_form = LoginForm
    success_message = "You are logged in successfully"


class LogoutUserView(LogoutView):
    next_page = '/'
