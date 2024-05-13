#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
import os

# Created by TrueSoer at 18.03.2024

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

from app.configuration.config import settings
from app.configuration.server import Server

def create_app(_=None) -> FastAPI:
    app = FastAPI()

    @app.get("/")
    async def index():
        return RedirectResponse(url="/api/v1/index")

    app.mount(
        "/static",
        StaticFiles(directory=os.path.join(settings.BASE_DIR, "app/static")),
        name="static",
    )


    return Server(app).get_app()
