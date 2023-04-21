from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from labels.models import Label
from labels.forms import CreateLabelForm


class LoginRequiredMixinWithFlash(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You are logged out. Please, log in.')
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class ListLabelsView(ListView):
    model = Label
    template_name = 'labels/list_labels.html'
    context_object_name = 'labels'


class CreateLabelsView(SuccessMessageMixin, LoginRequiredMixinWithFlash, CreateView):
    model = Label
    template_name = 'labels/label_create.html'
    form_class = CreateLabelForm
    success_url = reverse_lazy('list_labels')
    success_message = 'The label was created successfully'
    login_url = reverse_lazy('login')


class UpdateLabelsView(SuccessMessageMixin, LoginRequiredMixinWithFlash, UpdateView):
    model = Label
    pk_url_kwarg = 'label_id'
    template_name = 'labels/label_update.html'
    form_class = CreateLabelForm
    success_url = reverse_lazy('list_labels')
    success_message = "The label was changed successfully"
    login_url = reverse_lazy('login')


class DeleteLabelsView(SuccessMessageMixin, LoginRequiredMixinWithFlash, DeleteView):
    model = Label
    pk_url_kwarg = 'label_id'
    template_name = 'labels/label_delete.html'
    success_url = reverse_lazy('list_labels')
    success_message = "The label was deleted successfully"
    login_url = reverse_lazy('login')
    # TO DO check using status before deletion

