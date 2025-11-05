from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    tags = Column(String(600), nullable=True)  # comma-separated tags

    def __repr__(self):
        return f'[id={self.id}, name={self.name}, price={self.price}, stock={self.stock}, tags={self.tags}]'
