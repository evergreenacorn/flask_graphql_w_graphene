from sqlalchemy import (
    Column, DateTime, ForeignKey, Integer, String
)
from sqlalchemy.orm import backref, relationship, declarative_mixin


# Describe your models here


class Department:
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Role:
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employee:
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
