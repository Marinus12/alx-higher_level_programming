#!/usr/bin/python3
"""COntains the class definition of a State.
Inherits from SQLAlchemy Base and links to MySQL table states.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City

Base = declarative_base()

class State(Base):
    """State class to represent states table."""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
