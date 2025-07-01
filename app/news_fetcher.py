from newsapi import NewsApiClient
from app.database import SessionLocal
from app.models import News, NewsSource
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize News API client
newsapi = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))

# ✅ Function to fetch top headlines and store in database
def fetch_and_store_news():
    db = SessionLocal()
    try:
        response = newsapi.get_top_headlines(
            # q='bitcoin',              # Change as needed
            # category='business',
            language='en',
            country='us'
        )
        articles = response.get("articles", [])

        for article in articles:
            title = article.get("title")
            description = article.get("description")
            url = article.get("url")
            published_at = article.get("publishedAt")

            if title and url:
                existing = db.query(News).filter_by(url=url).first()
                if not existing:
                    news_item = News(
                        title=title,
                        description=description,
                        url=url,
                        published_at=datetime.fromisoformat(published_at.replace("Z", "+00:00"))
                    )
                    db.add(news_item)
        db.commit()
    except Exception as e:
        print(f"❌ Error fetching news: {e}")
    finally:
        db.close()

# ✅ Function to fetch available sources and store in database
def fetch_and_store_sources():
    db = SessionLocal()
    try:
        response = newsapi.get_sources(language="en", country="us")
        sources = response.get("sources", [])

        for src in sources:
            source_obj = NewsSource(
                id=src.get("id"),
                name=src.get("name"),
                description=src.get("description"),
                url=src.get("url"),
                category=src.get("category"),
                language=src.get("language"),
                country=src.get("country")
            )
            db.merge(source_obj)  # insert or update
        db.commit()
    except Exception as e:
        print(f"❌ Error fetching sources: {e}")
    finally:
        db.close()
