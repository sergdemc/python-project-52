from django.contrib.auth.forms import UserCreationForm
from users.models import User


class RegisterUsersForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'password1',
                  'password2']
