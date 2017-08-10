# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from . import token


class RedditConfig(AppConfig):
    name = 'reddit'


# 刷新间隔是3600秒，这里提前100秒
Timer(3500, token.refresh).start()