from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from statuses.models import Status
from statuses.forms import CreateStatusForm


class LoginRequiredMixinWithFlash(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You are logged out. Please, log in.')
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class ListStatusesView(ListView):
    model = Status
    template_name = 'statuses/list_statuses.html'
    context_object_name = 'statuses'


class CreateStatusesView(SuccessMessageMixin, LoginRequiredMixinWithFlash, CreateView):
    model = Status
    template_name = 'statuses/status_create.html'
    form_class = CreateStatusForm
    success_url = reverse_lazy('list_statuses')
    success_message = "The status was created successfully"
    login_url = reverse_lazy('login')


class UpdateStatusesView(SuccessMessageMixin, LoginRequiredMixinWithFlash, UpdateView):
    model = Status
    pk_url_kwarg = 'status_id'
    template_name = 'statuses/status_update.html'
    form_class = CreateStatusForm
    success_url = reverse_lazy('list_statuses')
    success_message = "The status was changed successfully"
    login_url = reverse_lazy('login')


class DeleteStatusesView(SuccessMessageMixin, LoginRequiredMixinWithFlash, DeleteView):
    model = Status
    pk_url_kwarg = 'status_id'
    template_name = 'statuses/status_delete.html'
    success_url = reverse_lazy('list_statuses')
    success_message = "The status was deleted successfully"
    login_url = reverse_lazy('login')
