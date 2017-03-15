#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy.types import Integer
from sqlalchemy.orm import relationship

class TableBuilder(object):

    def __init__(self, meta):
        self.meta = meta

    def many_to_many(self, left_class, right_class):
        self.add_table(left_class)
        self.add_table(right_class)
        l_table_name = left_class.__tablename__
        r_table_name = right_class.__tablename__
        r_table = Table('{0}_{1}'.format(l_table_name, r_table_name),
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

    def one_to_many(self, one_class, many_class):
        pass

    def one_to_one(self, left_class, right_class):
        pass

    def add_table(self, target_class):
        self.meta._add_table(name=target_class.__name__,
                             schema=self.meta.schema,
                             table=target_class.__table__
                             )

    def show_tabls(self):
        for i in Base.metadata.sorted_tables:
            print(i)

