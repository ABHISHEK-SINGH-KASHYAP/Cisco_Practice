from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from employee import Base, Employee

engine = create_engine('sqlite:///employees_db.sqlite', echo=True)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
