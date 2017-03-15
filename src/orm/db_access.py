#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.schema import CreateSchema
from sqlalchemy.sql import exists
from sqlalchemy.sql import select
from dto_base import Base
from dtos import ManyParent
from dtos import ManyChild
from dto_dto import OneChild
from dto_dto import OneChild
from table_builder import TableBuilder
import inspect



if __name__ == "__main__":

    engine = create_engine(
        'postgresql://foo_user:aaa@localhost/my_database', echo=True)

    # engine.execute('CREATE SCHEMA IF NOT EXISTS {0}'.format(schema))
    tb = TableBuilder(Base.metadata)
    tb.many_to_many(ManyChild, ManyParent)
    Base.metadata.create_all(engine)

