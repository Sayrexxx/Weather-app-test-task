from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import crud, models, database
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/weather", response_class=HTMLResponse)
async def get_weather(request: Request, city: str = Form(...), db: Session = Depends(get_db)):
    weather_data = crud.fetch_weather_data(city)
    if weather_data:
        crud.create_weather(db, city=city, temperature=weather_data["main"]["temp"], description=weather_data["weather"][0]["description"])
    return templates.TemplateResponse("index.html", {"request": request, "weather": weather_data})