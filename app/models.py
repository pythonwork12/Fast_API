from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

# 🔹 News Table
class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255))
    description = Column(String(500))
    url = Column(String(500), unique=True)
    published_at = Column(DateTime)

# 🔹 NewsSource Table
class NewsSource(Base):
    __tablename__ = "news_sources"

    id = Column(String(100), primary_key=True, index=True)  # 🔥 Use string ID
    name = Column(String(255))
    description = Column(String(500))
    url = Column(String(255))
    category = Column(String(100))
    language = Column(String(10))
    country = Column(String(10))
