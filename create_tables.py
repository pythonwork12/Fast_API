# create_tables.py

from app.database import Base, engine
from app.models import News, NewsSource

print("🛠 Creating tables in the database...")

Base.metadata.drop_all(bind=engine)     # ⚠️ Dev only: Drops old tables
Base.metadata.create_all(bind=engine)   # ✅ Creates new/updated tables

print("✅ Tables created successfully!")
