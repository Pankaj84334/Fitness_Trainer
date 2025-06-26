import pymysql
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine

def create_database():
    connection=pymysql.connect(
        host='localhost',
        user='root',
        password='Pankaj(6398536702)',
        database='fitness_trainer'
    )
    with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS fitness_trainer")
    connection.commit()
    connection.close()
create_database()
DATABASE_URL = "mysql+aiomysql://root:Pankaj(6398536702)@localhost/fitness_trainer"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()