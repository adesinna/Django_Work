from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Now we customise the form we get in views


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

