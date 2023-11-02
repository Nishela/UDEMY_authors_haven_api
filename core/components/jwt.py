from datetime import timedelta

from core.settings import env

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),  # Ожидаемый тип заголовка для JWT токена.
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "SIGNING_KEY": env("SIGNING_KEY"),  # Секретный ключ для подписи JWT токена.
    "USER_ID_FIELD": "id",  # Поле модели пользователя, которое будет использоваться для идентификации пользователя.
    "USER_ID_CLAIM": "user_id",  # Ключ в токене, который будет использоваться для идентификации пользователя.
}

REST_AUTH = {
    "USE_JWT": True,  # Использовать JWT токен для аутентификации.
    "JWT_AUTH_COOKIE": "authors-access-token",
    "JWT_AUTH_REFRESH_COOKIE": "authors-refresh-token",
    "REGISTER_SERIALIZER": "users.serializers.CustomRegisterSerializer",
    # Использовать кастомный сериализатор для регистрации.
}