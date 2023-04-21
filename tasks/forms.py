from django import forms
from django.utils.translation import gettext_lazy as _

from statuses.models import Status
from tasks.models import Task
from users.models import User


class CreateTaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label=_('Status'),
                                    widget=forms.widgets.Select(attrs={'class': 'form-control', }))
    executor = forms.ModelChoiceField(queryset=User.objects.all(), label=_('Executor'),
                                      widget=forms.widgets.Select(attrs={'class': 'form-control'}))
    # label = forms.ModelChoiceField(queryset=Status.objects.all(), label=_('Labels'),
    #                                widget=forms.widgets.Select(attrs={'class': 'form-control', 'size': 8}))

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor']
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': _('Name')}),
            'description': forms.widgets.Textarea(attrs={'class': 'form-control', 'placeholder': _('Description')})
        }

    def __init__(self, *args, **kwargs):
        super(CreateTaskForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''
