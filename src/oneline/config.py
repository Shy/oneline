from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

load_dotenv()

db_url = os.environ.get("DATABASE_URL").replace("postgresql://", "cockroachdb://")
try:
    engine = create_engine(db_url)
except Exception as e:
    print("Failed to connect to database.")
    print(f"{e}")
