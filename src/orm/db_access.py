#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer
from sqlalchemy.schema import CreateSchema
from sqlalchemy.sql import exists, select


engine = create_engine(
    'postgresql://foo_user:aaa@localhost/my_database', echo=True)

Base = declarative_base()
schema = "my_schema"
Base.metadata.schema = schema

engine.execute('CREATE SCHEMA IF NOT EXISTS {0}'.format(schema))
print(sqlalchemy.__version__)


class Parent(Base):

    """Docstring for Parent. """
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship('Child')

    def __repr__(self):
        return "<Parent(id={0})".format(self.id)


class Child(Base):

    """Docstring for Child. """
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent = relationship("Parent", back_populates="aaaa")

    def __repr__(self):
        return "<Parent(id={0})".format(self.id)

Base.metadata.create_all(engine)

