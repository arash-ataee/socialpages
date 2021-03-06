import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


@deconstructible
class ASCIIUsernameValidator(validators.RegexValidator):
    regex = r'^[\w.@+-]+\Z'
    message = _(
        'Enter a valid username. This value may contain only English letters, '
        'numbers, and @/./+/-/_ characters.'
    )
    flags = re.ASCII


@deconstructible
class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r'^[\w.@+-]+\Z'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and @/./+/-/_ characters.'
    )
    flags = 0


@deconstructible
class UnicodePhoneValidator(validators.RegexValidator):
    regex = r'(0|\+98)?([ ]|,|-|[()]){0,2}9[1|2|3|4]([ ]|,|-|[()]){0,2}(?:[0-9]([ ]|,|-|[()]){0,2}){8}'
    message = _(
        'Enter a valid phone number.'
    )
    flags = 0


@deconstructible
class HasDigitPasswordValidator(validators.RegexValidator):
    regex = r'(?=.*[0-9])'
    message = _(
        'Ensure string has minimum one digits.'
    )
    flags = 0


@deconstructible
class UppercasePasswordValidator(validators.RegexValidator):
    regex = r'(?=.*[A-Z])'
    message = _(
        'Ensure string has minimum one uppercase letters.'
    )
    flags = 0
