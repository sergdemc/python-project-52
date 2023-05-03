from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django import forms
from django_filters.views import FilterView
from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter

from task_manager.mixins import LoginRequiredMixinWithFlash, \
    TaskDeletionCheckMixin
from tasks.forms import CreateTaskForm
from tasks.models import Task
from labels.models import Label
from statuses.models import Status
from users.models import User


class TaskFilter(FilterSet):
    status = ModelChoiceFilter(queryset=Status.objects.all(),
                               label=_('Status'))
    executor = ModelChoiceFilter(queryset=User.objects.all(),
                                 label=_('Executor'))
    label = ModelChoiceFilter(queryset=Label.objects.all(),
                              label=_('Label'))

    self_tasks = BooleanFilter(
        widget=forms.CheckboxInput,
        method='get_self_tasks',
        label=_('Own tasks only')
    )

    def get_self_tasks(self, queryset, name, value):
        if value:
            author = getattr(self.request, 'user', None)
            return queryset.filter(author=author)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'label']


class ListTasksView(LoginRequiredMixinWithFlash,
                    FilterView):
    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter
    extra_context = {'button_text': _('Show')}


class CreateTasksView(LoginRequiredMixinWithFlash,
                      SuccessMessageMixin,
                      CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('list_tasks')
    success_message = _('The task was created successfully.')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTasksView(LoginRequiredMixinWithFlash,
                      SuccessMessageMixin,
                      UpdateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('list_tasks')
    success_message = _('The task was updated successfully.')
    pk_url_kwarg = 'pk'


class DeleteTasksView(LoginRequiredMixinWithFlash,
                      TaskDeletionCheckMixin,
                      SuccessMessageMixin,
                      DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('list_tasks')
    success_message = _('The task was deleted successfully')
    pk_url_kwarg = 'pk'


class DetailTasksView(LoginRequiredMixinWithFlash,
                      DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    pk_url_kwarg = 'pk'
