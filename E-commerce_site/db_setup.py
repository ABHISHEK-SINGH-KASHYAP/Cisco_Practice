from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from product import Base 

'''
import logging

# Reduce/no SQLAlchemy echo output in the terminal.
# Set echo=False to avoid printing raw SQL statements.
# Also raise the sqlalchemy.engine logger to WARNING to suppress INFO logs.
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

engine = create_engine('sqlite:///products_db.sqlite', echo=False)'''
#database for products
engine = create_engine('sqlite:///products_db.sqlite', echo=True)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
