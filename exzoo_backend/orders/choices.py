from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusChoices(models.TextChoices):
    PROCESSING: str = 'PR', _('Processing')
    COMPLETED: str = 'CO', _('Completed')
    CANCELED: str = 'CA', _('Canceled')
