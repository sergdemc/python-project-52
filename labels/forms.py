from django import forms
from django.utils.translation import gettext_lazy as _

from labels.models import Label


class CreateLabelForm(forms.ModelForm):

    class Meta:
        model = Label
        fields = ['name']
        widgets = {'name': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': _('Name')})}
        labels = {'name': _('Name')}

    def __init__(self, *args, **kwargs):
        super(CreateLabelForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''

