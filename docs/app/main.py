from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .routers import pages

app = FastAPI(title="Enterprise Card")

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Подключаем шаблоны
templates = Jinja2Templates(directory="app/templates")

# Подключаем роутеры
app.include_router(pages.router)

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})