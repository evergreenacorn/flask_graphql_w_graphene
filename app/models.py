from app import db
from sqlalchemy import (
    Column, DateTime, ForeignKey, Integer,
    String, func
)
from sqlalchemy.orm import backref, relationship, declarative_mixin


# Describe your models here


class Department(db.Model):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Role(db.Model):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employee(db.Model):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    role_id = Column(Integer, ForeignKey('roles.role_id'))
    department = relationship(
        Department,
        backref=backref(
            'employees',
            uselist=True,
            cascade='delete,all')
    )
    role = relationship(
        Role,
        backref=backref(
            'roles',
            uselist=True,
            cascade='delete,all')
    )
