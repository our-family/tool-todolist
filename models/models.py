from sqlalchemy import Column, Integer, String
from models.db import engine, Base


class Items(Base):
    __tablename__ = 'Items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(String)
    title = Column(String)
    context = Column(String)
    status = Column(String)
    finish = Column(String)

    def __repr__(self):
        return "<Items(id='%s', title='%s')>" % (self.id, self.title)


Base.metadata.create_all(engine)
