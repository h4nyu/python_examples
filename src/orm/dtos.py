#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import RelationshipProperty
from dto_base import Base


class ManyParent(Base):

    """Docstring for Parent. """
    __tablename__ = 'many_parent'
    id = Column(Integer, primary_key=True)
    children = relationship('ManyChild')

    def __repr__(self):
        return "<Parent(id={0})".format(self.id)


class ManyChild(Base):

    """Docstring for Child. """
    __tablename__ = 'many_child'
    id = Column(Integer, primary_key=True)
    parent = relationship('ManyParent',  back_populates="children")

    def __repr__(self):
        return "<Parent(id={0})".format(self.id)
