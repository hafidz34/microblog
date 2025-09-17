import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        user = os.getenv("PGUSER", "postgres")
        pwd  = quote_plus(os.getenv("PGPASSWORD", "postgres"))
        host = os.getenv("PGHOST", "127.0.0.1")
        port = os.getenv("PGPORT", "5432")
        db   = os.getenv("PGDATABASE", "microblog")
        db_url = f"postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}"

    SQLALCHEMY_DATABASE_URI = db_url
