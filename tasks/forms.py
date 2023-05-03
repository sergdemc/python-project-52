from django.forms import widgets, ModelForm, \
    ModelChoiceField, ModelMultipleChoiceField
from django.utils.translation import gettext_lazy as _

from statuses.models import Status
from tasks.models import Task
from users.models import User
from labels.models import Label


class CreateTaskForm(ModelForm):
    status = ModelChoiceField(
        queryset=Status.objects.all(),
        label=_('Status'),
        widget=widgets.Select(
            attrs={'class': 'form-control'})
    )
    executor = ModelChoiceField(
        queryset=User.objects.all(),
        label=_('Executor'),
        required=False,
        widget=widgets.Select(attrs={'class': 'form-control'})
    )
    label = ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        label=_('Labels'),
        required=False,
        widget=widgets.SelectMultiple(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'label']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control',
                                             'placeholder': _('Name')}),
            'description': widgets.Textarea(attrs={'class': 'form-control',
                                                   'placeholder': _('Description')})  # noqa: 501
        }
        labels = {'name': _('Name'), 'description': _('Description')}

    def __init__(self, *args, **kwargs):
        super(CreateTaskForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''
