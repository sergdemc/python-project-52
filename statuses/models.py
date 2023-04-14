from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    name = models.CharField(_('name'), max_length=100, unique=True)
    created_at = models.DateTimeField(_('created date'), auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name_plural = _("statuses")

    def __str__(self):
        return self.name
