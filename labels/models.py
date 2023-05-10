from django.db import models
from django.utils.translation import gettext_lazy as _


class Label(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Name')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at')
    )

    def can_be_deleted(self):
        return not self.task_set.exists()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_at"]
        verbose_name = _('Label')
        verbose_name_plural = _('Labels')
