from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend #, BaseBackend
from django.db.models import Q


User = get_user_model()


class UsernameOrEmailLoginModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        auth_type = settings.AUTH_AUTHENTICATION_TYPE
        if auth_type == 'username':
            # use the default authenticate method
            # try to query a user if extending from BaseBackend
            return super().authenticate(request, username=username, password=password, **kwargs)
        else:
            try:
                if auth_type == 'both':
                    user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
                else:
                    # check the email aginst the 'username' argument
                    user = User.objects.get(email__iexact=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                return None
    # implement this method if extending the backend from BaseBackend
    # def get_user(self, user_id):
    #     try:
    #         return User.objects.get(pk=user_id)
    #     except User.DoesNotExist:
    #         return None
