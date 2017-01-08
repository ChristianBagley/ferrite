from sqlalchemy import Column, Integer, String, types
from database import Base


class Visit(Base):
    __tablename__ = 'visits'

    id = Column(Integer, primary_key=True)
    url = Column(String(500))
    time = Column(types.DateTime())
    raw_dom = Column(types.Text())
    extacted_text = Column(types.Text())
    lang = Column(String(16))

    def __init__(self, url, time, raw_dom):
        self.url = url
        self.time = time
        self.raw_dom = raw_dom

    def __repr__(self):
        return '<Visit %s>' % (self.url[:20])
