from django.forms import widgets, ModelForm
from django.utils.translation import gettext_lazy as _

from statuses.models import Status


class CreateStatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {'name': widgets.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': _('Name')})}
        labels = {'name': _('Name')}

    def __init__(self, *args, **kwargs):
        super(CreateStatusForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''
