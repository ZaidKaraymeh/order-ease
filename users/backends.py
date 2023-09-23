from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class EmailOrPhoneNumberModelBackend(ModelBackend):
    """
    This is a ModelBacked that allows authentication
    with either a username or an email address.
    
    """
    def authenticate(self, username='None', password='None'):
        if '@' in username:
            kwargs = {'email': username}
        elif username.isnumeric():
            kwargs = {'phone_number': username}
        else:
            kwargs = {'username': username}
        try:
            user = CustomUser.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, username):
        try:
            return get_user_model().objects.get(pk=username)
        except get_user_model().DoesNotExist:
            return None
