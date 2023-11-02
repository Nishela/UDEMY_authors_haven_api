__all__ = ("UserSerializer",)

from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="profile.gender")
    phone_number = PhoneNumberField(source="profile.phone_number")
    profile_photo = serializers.ReadOnlyField(source="profile.profile_photo.url")
    country = CountryField(source="profile.country")
    city = serializers.CharField(source="profile.city")
    is_admin = serializers.BooleanField(source="is_superuser", read_only=True)

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "gender",
            "phone_number",
            "profile_photo",
            "country",
            "city",
            "is_admin"
        )
