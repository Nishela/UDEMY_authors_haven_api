AUTHENTICATION_BACKENDS = [
    "allauth.account.auth_backends.AuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend",
]

ACCOUNT_AUTHENTICATION_METHOD = "email"  # Использовать email для аутентификации.
ACCOUNT_EMAIL_REQUIRED = True  # Обязательно указывать email при регистрации.
ACCOUNT_EMAIL_VERIFICATION = "mandatory"  # Обязательно подтверждать email.
ACCOUNT_CONFIRM_EMAIL_ON_GET = True  # Подтверждать email при переходе по ссылке.
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1  # Срок действия ссылки для подтверждения email.
ACCOUNT_USER_MODEL_USERNAME_FIELD = None  # Не использовать username.
ACCOUNT_USERNAME_REQUIRED = False  # Не использовать username.