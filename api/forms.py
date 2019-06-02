from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import NyteUser


class NyteUserCreationForm(UserCreationForm):
    class Meta:
        model = NyteUser
        fields = "__all__"

class NyteUserChangeForm(UserChangeForm):
    class Meta:
        model = NyteUser
        fields = "__all__"