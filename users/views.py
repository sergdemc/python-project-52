from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from task_manager.mixins import UserPermissionCheckMixin, \
    LoginRequiredMixinWithFlash, UserDeletionPermissionMixin
from users.models import User
from users.forms import RegisterUsersForm, LoginForm


class ListUsersView(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'


class UpdateUsersView(SuccessMessageMixin,
                      LoginRequiredMixinWithFlash,
                      UserPermissionCheckMixin,
                      UpdateView):
    model = User
    form_class = RegisterUsersForm
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('list_users')
    pk_url_kwarg = 'pk'
    success_message = _('The user was updated successfully.')


class DeleteUsersView(LoginRequiredMixinWithFlash,
                      SuccessMessageMixin,
                      UserDeletionPermissionMixin,
                      UserPermissionCheckMixin,
                      DeleteView):
    model = User
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy('list_users')
    pk_url_kwarg = 'pk'
    success_message = _('The user was deleted successfully.')


class RegisterUsersView(SuccessMessageMixin,
                        CreateView):
    model = User
    template_name = 'users/user_create.html'
    form_class = RegisterUsersForm
    success_url = reverse_lazy('login')
    success_message = _('The user was created successfully.')


class LoginUserView(SuccessMessageMixin,
                    LoginView):
    template_name = 'users/login.html'
    next_page = '/'
    authentication_form = LoginForm
    success_message = _('You are logged in successfully.')

    def form_invalid(self, form):
        messages.error(
            self.request, _('Please enter the correct username and password. '
                            'Both fields can be case sensitive.')
        )
        return super(LoginUserView, self).form_invalid(form)


class LogoutUserView(LogoutView):
    next_page = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, _('You have successfully logged out.'))
        return super().dispatch(request, *args, **kwargs)
