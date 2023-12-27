from sqlalchemy import create_engine, Column, Integer, String, Double, MetaData, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta

Base = declarative_base()

ONE_DAY_IN_MINUTES = 1440

class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nm_price = Column(Double)
    ex_price = Column(Double)
    vg_price = Column(Double)
    g_price = Column(Double)
    edition = Column(String)
    timestamp = Column(DateTime, default=func.now(), onupdate=func.current_timestamp())

    def __init__(self, name, price, edition, timestamp=func.now()):
      self.name = name
      self.nm_price = price['nm']
      self.ex_price = price['ex']
      self.vg_price = price['vg']
      self.g_price = price['g']
      self.edition = edition
      self.timestamp = timestamp
    
    def to_dict(self):
      return { 'name': self.name, 'prices': {
        'nm': self.nm_price,
        'ex': self.ex_price,
        'vg': self.vg_price,
        'g': self.g_price
      }, 'edition': self.edition }

    def is_fresh(self):
      current_time = datetime.utcnow()
      age = current_time - self.timestamp
      max_age = timedelta(minutes=ONE_DAY_IN_MINUTES)

      return age < max_age