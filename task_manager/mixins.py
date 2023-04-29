from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect, reverse
from django.db import models

from tasks.models import Task


class LoginRequiredMixinWithFlash(LoginRequiredMixin):
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('You are logged out. Please, log in.'))
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class UserPermissionCheckMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != request.resolver_match.kwargs['user_id']:
            messages.error(request, _('You do not have rights to change another user.'))
            return redirect(reverse('list_users'))
        return super().dispatch(request, *args, **kwargs)


class TaskDeletionCheckMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        task_id = request.resolver_match.kwargs['task_id']
        author_id = Task.objects.get(id=task_id).author.pk
        if request.user.pk != author_id:
            messages.error(request, _('A task can only be deleted by its author.'))
            return redirect(reverse('list_tasks'))
        return super().dispatch(request, *args, **kwargs)


class UserDeletionPermissionMixin:
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(self.request, _('The user was deleted successfully.'))
        except models.ProtectedError:
            messages.error(self.request, _('Cannot delete user because it is in use.'))
        finally:
            return redirect(reverse('list_users'))
