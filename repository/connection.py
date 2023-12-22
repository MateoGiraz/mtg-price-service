from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model.card import Base

def connect(db_url):
  engine = create_engine(db_url, echo=True)

  Session = sessionmaker(bind=engine)
  session = Session()

  Base.metadata.create_all(bind=engine)

  return session
