from sqlalchemy import create_engine, Column, Integer, String, Double, MetaData, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta

Base = declarative_base()

ONE_DAY_IN_MINUTES = 1440

class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Double)
    timestamp = Column(DateTime, default=func.now(), onupdate=func.current_timestamp())

    def __init__(self, name, price, timestamp=func.now()):
      self.name = name
      self.price = price
      self.timestamp = timestamp
    
    def to_dict(self):
      return { 'name': self.name, 'price': self.price }

    def is_fresh(self):
      current_time = datetime.utcnow()
      age = current_time - self.timestamp
      max_age = timedelta(minutes=ONE_DAY_IN_MINUTES)

      return age < max_age