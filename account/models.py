from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import *
# Create your models here.

@python_2_unicode_compatible
class Account(models.Model):
    account = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    p_key = models.CharField(max_length=100, blank=True, null=True)
    group = models.ForeignKey(Group, null=True)
    owner = models.ForeignKey(User, null=True)

    def __str__(self):
        return str(self.owner)
        


