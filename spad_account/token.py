from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils import six
import six
# try:
#     # six removed since Django 3.0
# from django.utils import six
# except ImportError:
#     import six
#     import sys
#     sys.modules["django.utils.six"] = six
#     # similarly for any other six sub-module required:
#     sys.modules["django.utils.six.moves"] = six.moves


# finally, import the outdated third-party package below:

# import outdated_library

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
        )
account_activation_token = TokenGenerator()