#!/usr/bin/python3
"""
This module defines a State class that maps to the 'states' table
in a database using SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that maps to the 'states' table in the database
    with columns 'id' and 'name'.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
