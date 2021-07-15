from sqlalchemy import (
    Column, DateTime, ForeignKey, Integer,
    String, func
)
from sqlalchemy.orm import (
    backref, relationship, declarative_mixin,
    declared_attr
)
from datetime import datetime
from app import db


# Describe your models here
@declarative_mixin
class StandartModelMixin:
    id = Column(Integer, primary_key=True)
    name = Column(String)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class TimestampMixin:
    created = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    updated = Column(
        DateTime,
        onupdate=datetime.utcnow
    )


class Department(StandartModelMixin, TimestampMixin, db.Model): ...


class Role(StandartModelMixin, TimestampMixin, db.Model): ...


class Employee(StandartModelMixin, TimestampMixin, db.Model):
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
