from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(50), nullable=False)


class Email(Base):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)
    contact_id = Column(Integer, ForeignKey(Contact.id, ondelete="CASCADE"))


class Phone(Base):
    __tablename__ = "phones"
    id = Column(Integer, primary_key=True)
    phone = Column(String(20), nullable=False)
    contact_id = Column(Integer, ForeignKey(Contact.id, ondelete="CASCADE"))
