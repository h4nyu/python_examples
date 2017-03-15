#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import Table
from sqlalchemy.schema import CreateSchema
from sqlalchemy.sql import exists
from sqlalchemy.sql import select
from dto_base import Base
from dto_base import engine
from dtos import Parent
from dtos import Child
from sqlalchemy.orm import sessionmaker


# Base.metadata.reflect(engine, extend_existing=True)


if __name__ == "__main__":
    # engine.execute('CREATE SCHEMA IF NOT EXISTS {0}'.format(schema))
    for i in Base.metadata.tables:
        print(i)
    Base.metadata.create_all()
    Session = sessionmaker(bind=engine)
    session = Session()
    mp = Parent(name='iam')
    chidren = []
    for i in range(3):
        chidren.append(Child(name="{0}aa".format(i)))

    mp.children = chidren
    c = Child(name='i have 10 parent')
    parents = []
    for i in range(10):
        parents.append(Parent(name="bbb{0}".format(i)))
    c.parents = parents

    session.add(mp)
    session.add(c)
    session.commit()
