from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Float, create_engine

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    job_title = Column(String(150), nullable=False)
    salary = Column(Float, nullable=False)
    
    def __repr__(self):
        return f'[id = {self.id}, name = {self.name}, job_title = {self.job_title}, salary = {self.salary}]'
    
#setup database
engine = create_engine('sqlite:///employees_db.sqlite',echo=True) #create database if not exist
Base.metadata.create_all(engine)

#setup the things for the transactions(create, read, update, delete)
Sessionlocal = sessionmaker(bind=engine)
session = Sessionlocal()

#crudops
dravid = Employee(name = 'Dravid', job_title = 'Batsman', salary = 1200)
session.add(dravid)
session.commit()

