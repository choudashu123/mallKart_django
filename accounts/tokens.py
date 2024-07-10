# tokens.py
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        login_timestamp = '' if user.last_login is None else user.last_login
        return f"{user.pk}{user.password}{login_timestamp}{timestamp}"

account_activation_token = AccountActivationTokenGenerator()
