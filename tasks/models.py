from django.utils.translation import gettext_lazy as _
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey('users.User', on_delete=models.PROTECT, related_name='authored_tasks')
    description = models.TextField(blank=True)
    status = models.ForeignKey('statuses.Status', on_delete=models.PROTECT)
    executor = models.ForeignKey(
        'users.User', on_delete=models.PROTECT, blank=True,
        related_name='executed_tasks')
    label = models.ManyToManyField('labels.Label', blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name
