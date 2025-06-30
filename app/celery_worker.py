from celery import shared_task
from app.news_fetcher import fetch_and_store_news,fetch_and_store_sources

@shared_task(name="fetch_news_task")  # ✅ Name helps identify
def fetch_news_task():
    fetch_and_store_news()
    fetch_and_store_sources()