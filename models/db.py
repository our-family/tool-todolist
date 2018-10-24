from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


engine = create_engine('sqlite:///database')
Base = declarative_base()
Session = Session(bind=engine)

