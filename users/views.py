from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from users.models import User
from users.forms import RegisterUsersForm, LoginForm


class UserPermissionCheckMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != request.resolver_match.kwargs['user_id']:
            messages.error(request, 'You do not have rights to change another user.')
            return redirect(reverse('list_users'))
        return super().dispatch(request, *args, **kwargs)


class LoginRequiredMixinWithFlash(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You are logged out. Please, log in.')
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class ListUsersView(ListView):
    model = User
    template_name = 'users/list_users.html'
    context_object_name = 'users'


class UpdateUsersView(SuccessMessageMixin, LoginRequiredMixinWithFlash, UserPermissionCheckMixin, UpdateView):
    model = User
    form_class = RegisterUsersForm
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('list_users')
    pk_url_kwarg = "user_id"
    login_url = reverse_lazy('login')
    success_message = "The user was updated successfully"


class DeleteUsersView(SuccessMessageMixin, LoginRequiredMixinWithFlash, UserPermissionCheckMixin, DeleteView):
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

    def form_invalid(self, form):
        messages.error(self.request, 'Please enter the correct username and password. Both fields can be case sensitive.')
        return super(LoginUserView, self).form_invalid(form)


class LogoutUserView(LogoutView):
    next_page = '/'


