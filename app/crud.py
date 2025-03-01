import requests
from dotenv import load_dotenv
import os
from sqlalchemy.orm import Session
from . import models

load_dotenv()

def fetch_weather_data(city: str):
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def create_weather(db: Session, city: str, temperature: float, description: str):
    db_weather = models.Weather(city=city, temperature=temperature, description=description)
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather

def get_weather_history(db: Session):
    return db.query(models.Weather).order_by(models.Weather.timestamp.desc()).all()