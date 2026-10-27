#!/usr/bin/python3
"""Module: Using SQLAlchemy as an ORM."""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """This is the model state that will be used in the project"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
