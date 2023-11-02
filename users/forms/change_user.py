__all__ = ("ChangeUserForm",)

from django.contrib.auth.forms import UserChangeForm, get_user_model


class ChangeUserForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
