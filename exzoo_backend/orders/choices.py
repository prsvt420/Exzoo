from django.db import models
from django.utils.translation import gettext_lazy as _
from django_stubs_ext import StrPromise


class StatusChoices(models.TextChoices):
    PROCESSING: tuple[str, StrPromise] = 'PR', _('Processing')
    COMPLETED: tuple[str, StrPromise] = 'CO', _('Completed')
    CANCELED: tuple[str, StrPromise] = 'CA', _('Canceled')
