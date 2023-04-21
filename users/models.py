from django.contrib.auth.models import AbstractUser
from django.contrib import messages
from django.shortcuts import redirect, reverse

from django.db import models


class User(AbstractUser):
    pass
    # def delete(self, using=None, keep_parents=False):
    #     if self.authored_tasks.exists() or self.executed_tasks.exists():
    #         raise models.ProtectedError("Cannot delete user because there are tasks associated with it",
    #                                     self.authored_tasks.all() | self.executed_tasks.all())
    #     super().delete(using=using, keep_parents=keep_parents)
