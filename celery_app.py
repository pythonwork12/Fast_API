from celery import Celery

# Create Celery app instance
app = Celery(
    "app",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

# Configure beat schedule
app.conf.beat_schedule = {
    "fetch-news-every-minute": {
        "task": "fetch_news_task",   # ✅ Match task name here
        "schedule": 60.0,
    },
}

app.conf.timezone = 'UTC'

# ✅ Import tasks AFTER app is created so they can register correctly
from app import celery_worker
