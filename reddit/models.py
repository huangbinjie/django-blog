# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Reddit(models.Model):
    token_type = models.CharField(max_length=10)
    access_token = models.CharField(max_length=500)
