#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy.types import Integer
from sqlalchemy.orm import relationship
import inspect


class RelationPlaceholder(object):

    def __init__(self, class_name, back_populates):
        self.target_class = class_name
        self.back_populates = back_populates

    def __repr__(self):
        return "<RelationPlaceholder(target={0})".format(self.target_class)


def get_intermediate_table(meta, left, right):
    return Table("{0}_{1}".format(left, right),
                 meta,
                 Column('{0}_id'.format(left),
                        Integer,
                        ForeignKey('{0}.id'.format(left))
                        ),
                 Column('{0}_id'.format(right),
                        Integer,
                        ForeignKey('{0}.id'.format(right))
                        ),
                 )


class TableBuilder(object):

    def __init__(self, meta):
        self.meta = meta

    def many_to_many(self, left_class, right_class):
        self.add_table(left_class)
        self.add_table(right_class)
        l_table_name = left_class.__tablename__
        r_table_name = right_class.__tablename__
        r_table = Table(get_intermediate_table_name(left_class,
                                                    right_class),
                        self.meta,
                        Column('{0}_id'.format(l_table_name),
                               Integer,
                               ForeignKey('{0}.id'.format(l_table_name))
                               ),
                        Column('{0}_id'.format(r_table_name),
                               Integer,
                               ForeignKey('{0}.id'.format(r_table_name))
                               ),
                        )
        left_class.__table_args__ = {'secondary': r_table}
        right_class.__table_args__ = {'secondary': r_table}

        for i in inspect.getmembers(right_class):
            if isinstance(i[1], RelationPlaceholder):
                if i[1].target_class == left_class.__name__:
                    relation = relationship(left_class.__name__,
                                            secondary=r_table,
                                            back_populates=i[1].back_populates
                                            )
        for i in inspect.getmembers(left_class):
            if isinstance(i[1], RelationPlaceholder):
                if i[1].target_class == right_class.__name__:
                    relation = relationship(right_class.__name__,
                                            secondary=r_table,
                                            back_populates=i[1].back_populates
                                            )

    def one_to_many(self, one_class, many_class):
        raise NotImplementedError()

    def one_to_one(self, left_class, right_class):
        raise NotImplementedError()

    def add_table(self, target_class):
        self.meta._add_table(name=target_class.__tablename__,
                             schema=self.meta.schema,
                             table=target_class.__table__
                             )

    def show_tables(self):
        for i in self.meta.sorted_tables:
            print(i)
