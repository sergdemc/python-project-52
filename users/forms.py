from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User


class RegisterUsersForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'password1',
                  'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterUsersForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control',
                                                       'placeholder': _('First name')})  # noqa: 501
        self.fields['last_name'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder': _('Last name')})  # noqa: 501
        self.fields['username'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder': _('Username')})  # noqa: 501
        self.fields['password1'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder': _('Password')})  # noqa: 501
        self.fields['password2'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder': _('Password confirmation')})  # noqa: 501
        self.label_suffix = ''


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder': _('Username')})  # noqa: 501
        self.fields['password'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder': _('Password')})  # noqa: 501
        self.label_suffix = ''
