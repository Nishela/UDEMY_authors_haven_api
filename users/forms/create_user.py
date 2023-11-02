__all__ = ("CreateUserForm",)

from django.contrib.auth.forms import UserCreationForm, get_user_model
from django.forms import ValidationError

User = get_user_model()


class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email')

    error_messages = {
        "duplicate_email": "A user with that email already exists.",
    }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                message=self.error_messages["duplicate_email"],
                code="duplicate_email",
            )
        return email
