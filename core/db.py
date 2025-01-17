import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from core.models import Base
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)


def create_database():
    """Создает таблицы в БД"""
    try:
      # Проверяем существование папки `data`
      data_dir = os.path.dirname(DATABASE_URL.split("sqlite:///")[-1])
      if not os.path.exists(data_dir):
        os.makedirs(data_dir)

      Base.metadata.create_all(engine)
      print("Database created successfully")
    except OperationalError as e:
        print(f"Error creating database: {e}")
def get_session():
    """Возвращает сессию для работы с БД"""
    return Session()