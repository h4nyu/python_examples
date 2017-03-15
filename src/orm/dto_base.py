#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://foo_user:aaa@localhost/my_database')
Base = declarative_base(bind=engine)
Base.metadata.schema = "my_schema"
