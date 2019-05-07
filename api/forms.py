from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import NyteUser


class NyteUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = NyteUser
        fields = ('email', 'birthday',)

class NyteUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = NyteUser
        fields = ('email', 'birthday', )