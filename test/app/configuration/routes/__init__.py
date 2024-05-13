#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

# Created by TrueSoer at 18.03.2024


from app.configuration.routes.routes import *
from app.internal.routes import user, pages

__routes__ = Routes(routers=(user.router, pages.router))