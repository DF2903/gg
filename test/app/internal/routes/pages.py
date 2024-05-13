from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
import os

from starlette.responses import HTMLResponse

from app.configuration.config import settings

router = APIRouter(prefix='/api/v1')

templates = Jinja2Templates(directory=os.path.join(settings.BASE_DIR, "app/templates"))

@router.get('/index', status_code=200)
async def get_index(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@router.get("/scroll/{checking_type}", status_code=200)
async def get_scroll_page(request: Request, checking_type: str):
    return templates.TemplateResponse("scroll.html", {"request": request, "checking_type": checking_type})

@router.get("/starknet/{checking_type}", status_code=200)
async def get_starknet_page(request: Request, checking_type: str):
    return templates.TemplateResponse("starknet.html", {"request": request, "checking_type": checking_type})

@router.post("/scroll", response_class=HTMLResponse)
async def post_scroll_info(request: Request, textarea_wallets: str = Form(default='')):
    key = f"возвращаем ключи: {textarea_wallets}"
    return templates.TemplateResponse("scroll.html", {"request": request, "key": key})
