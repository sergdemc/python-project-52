from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Name')
    )
    author = models.ForeignKey(
        'users.User',
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name=_('Author')

    )
    description = models.TextField(
        blank=True,
        verbose_name=_('Description')
    )
    status = models.ForeignKey(
        'statuses.Status',
        on_delete=models.PROTECT,
        verbose_name=_('Status'),
        related_name='status'
    )
    executor = models.ForeignKey(
        'users.User',
        on_delete=models.PROTECT,
        blank=True,
        related_name='executor',
        null=True,
        verbose_name=_('Executor')
    )
    label = models.ManyToManyField(
        'labels.Label',
        blank=True,
        default=None,
        related_name='labels',
        verbose_name=_('Labels')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at')
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_at"]
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
