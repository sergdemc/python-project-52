from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _

from task_manager.mixins import LoginRequiredMixinWithFlash
from statuses.models import Status
from statuses.forms import CreateStatusForm


class ListStatusesView(ListView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'


class CreateStatusesView(SuccessMessageMixin,
                         LoginRequiredMixinWithFlash,
                         CreateView):
    model = Status
    template_name = 'statuses/status_create.html'
    form_class = CreateStatusForm
    success_url = reverse_lazy('list_statuses')
    success_message = _('The status was created successfully.')


class UpdateStatusesView(SuccessMessageMixin,
                         LoginRequiredMixinWithFlash,
                         UpdateView):
    model = Status
    pk_url_kwarg = 'pk'
    template_name = 'statuses/status_update.html'
    form_class = CreateStatusForm
    success_url = reverse_lazy('list_statuses')
    success_message = _('The status was changed successfully.')


class DeleteStatusesView(SuccessMessageMixin,
                         LoginRequiredMixinWithFlash,
                         DeleteView):
    model = Status
    pk_url_kwarg = 'pk'
    template_name = 'statuses/status_delete.html'
    success_url = reverse_lazy('list_statuses')
    success_message = _('The status was deleted successfully.')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.task_set.exists():
            messages.error(request, _("The status can't be deleted as it's used."))   # noqa: 501
            return HttpResponseRedirect(reverse_lazy('list_statuses'))
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
