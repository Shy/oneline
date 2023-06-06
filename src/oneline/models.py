from dataclasses import dataclass
from sqlalchemy.orm import declarative_base
from .db import DB

from sqlalchemy import Column, Text, DateTime, ForeignKey, Date, func
from sqlalchemy.dialects.postgresql import UUID

db = DB.create()
engine = db.engine
Base = declarative_base()


@dataclass
class Person(Base):
    __tablename__ = "person"
    id = Column(UUID(as_uuid=True), primary_key=True)
    username = Column(Text, unique=True)
    phone = Column(Text, unique=True)
    created_on = Column(DateTime, server_default=func.now())
    last_login = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return "<Person {}>".format(self.username)


class Line(Base):
    __tablename__ = "line"
    id = Column(UUID(as_uuid=True), primary_key=True)
    person = Column(UUID(as_uuid=True), ForeignKey("person.id"))
    line = Column(Text)
    created_on = Column(DateTime, server_default=func.now())
    edited_on = Column(DateTime, server_default=func.now(), onupdate=func.now())
    line_date = Column(Date)

    def __repr__(self):
        return "<Line {}>".format(self.line)
