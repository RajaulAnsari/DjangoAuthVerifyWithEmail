from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
