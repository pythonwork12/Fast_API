from fastapi import FastAPI
from app.models import News
from app.database import SessionLocal

app = FastAPI()

@app.get("/news")
def get_news():
    db = SessionLocal()
    news = db.query(News).order_by(News.published_at.desc()).all()
    return news
