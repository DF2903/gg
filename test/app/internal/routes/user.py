#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

# Created by TrueSoer at 18.03.2024


from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

router = APIRouter(prefix='/api/v1')

path = '/app/templates'
templates = Jinja2Templates(directory=path)
@router.get('/base')
def user_hello(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})
