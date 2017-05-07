#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio


def test_is_async():
    async def hello_world():
        print("hello world")
    print(asyncio.iscoroutine(hello_world()))
