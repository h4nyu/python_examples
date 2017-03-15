#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey
from sqlalchemy import Table
from sqlalchemy.types import Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import RelationshipProperty
from sqlalchemy.dialects.postgresql import TEXT
from dto_base import Base
from table_builder import get_intermediate_table

class_table_names = {
    "Parent": "parent",
    "Child": "child",
}


r_table = get_intermediate_table(Base.metadata,
                                 class_table_names['Parent'],
                                 class_table_names['Child'])


class Parent(Base):

    """Docstring for Parent. """
    __tablename__ = class_table_names['Parent']
    id = Column(Integer, primary_key=True)
    name = Column(TEXT)
    children = relationship('Child',
                            secondary=r_table,
                            back_populates="parents")

    def __repr__(self):
        return "<Parent(id={0})".format(self.id)


class Child(Base):

    """Docstring for Child. """
    __tablename__ = class_table_names['Child']
    id = Column(Integer, primary_key=True)
    name = Column(TEXT)
    parents = relationship('Parent',
                           secondary=r_table,
                           back_populates="children")

    def __repr__(self):
        return "<Parent(id={0})".format(self.id)
