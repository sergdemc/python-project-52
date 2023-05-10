from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _

from task_manager.mixins import LoginRequiredMixinWithFlash
from labels.models import Label
from labels.forms import LabelForm


class ListLabelsView(ListView):
    model = Label
    template_name = 'labels/labels.html'
    context_object_name = 'labels'


class CreateLabelsView(SuccessMessageMixin,
                       LoginRequiredMixinWithFlash,
                       CreateView):
    model = Label
    template_name = 'labels/label_create.html'
    form_class = LabelForm
    success_url = reverse_lazy('list_labels')
    success_message = _('The label was created successfully')
    extra_context = {'button_text': _('Create')}


class UpdateLabelsView(SuccessMessageMixin,
                       LoginRequiredMixinWithFlash,
                       UpdateView):
    model = Label
    pk_url_kwarg = 'pk'
    template_name = 'labels/label_update.html'
    form_class = LabelForm
    success_url = reverse_lazy('list_labels')
    success_message = _('The label was changed successfully')
    extra_context = {'button_text': _('Change')}


class DeleteLabelsView(SuccessMessageMixin,
                       LoginRequiredMixinWithFlash,
                       DeleteView):
    model = Label
    pk_url_kwarg = 'pk'
    template_name = 'labels/label_delete.html'
    success_url = reverse_lazy('list_labels')
    success_message = _('The label was deleted successfully')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.task_set.exists():
            messages.error(request, _("The label can't be deleted as it's used"))  # noqa: 501
            return HttpResponseRedirect(reverse_lazy('list_labels'))
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
