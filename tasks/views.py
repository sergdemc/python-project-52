from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect, reverse

from tasks.forms import CreateTaskForm
from tasks.models import Task
from statuses.models import Status
from users.models import User


class LoginRequiredMixinWithFlash(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You are logged out. Please, log in.')
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class TaskDeletionCheckMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        task_id = request.resolver_match.kwargs['task_id']
        author_id = Task.objects.get(id=task_id).author.pk
        if request.user.pk != author_id:
            messages.error(request, 'A task can only be deleted by its author.')
            return redirect(reverse('list_tasks'))
        return super().dispatch(request, *args, **kwargs)


class ListTasksView(LoginRequiredMixinWithFlash, ListView):
    model = Task
    template_name = 'tasks/list_tasks.html'
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        statuses = Status.objects.all()
        users = User.objects.all()
        context = {'statuses': statuses, 'users': users}
        return super(ListTasksView, self).get_context_data(**context)


class CreateTasksView(LoginRequiredMixinWithFlash, SuccessMessageMixin, CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('list_tasks')
    success_message = 'The task was created successfully'
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTasksView(LoginRequiredMixinWithFlash, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('list_tasks')
    success_message = 'The task was updated successfully'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'task_id'


class DeleteTasksView(LoginRequiredMixinWithFlash, TaskDeletionCheckMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('list_tasks')
    success_message = "The task was deleted successfully"
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'task_id'


class DetailTasksView(LoginRequiredMixinWithFlash, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    pk_url_kwarg = 'task_id'
