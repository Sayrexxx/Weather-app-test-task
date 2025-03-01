from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .crud import fetch_weather_data

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/weather", response_class=HTMLResponse)
async def get_weather(request: Request, city: str = Form(...)):
    weather_data = fetch_weather_data(city)
    return templates.TemplateResponse("index.html", {"request": request, "weather": weather_data})