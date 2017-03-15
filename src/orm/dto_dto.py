#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import RelationshipProperty
from dto_base import Base

schema = "my_schema"


class OneParent(Base):

    """Docstring for Parent. """
    __tablename__ = 'one_parent'
    __table_args__ = {'schema': schema}
    id = Column(Integer, primary_key=True)
    children = relationship('ManyChild')

    def __repr__(self):
        return "<Parent(id={0})".format(self.id)


class OneChild(Base):

    """Docstring for Child. """
    __tablename__ = 'one_child'
    __table_args__ = {'schema': schema}
    id = Column(Integer, primary_key=True)
    parent = relationship('ManyParent',  back_populates="children")

    def __repr__(self):
        return "<Parent(id={0})".format(self.id)



