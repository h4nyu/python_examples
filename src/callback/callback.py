#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MyClass(object):

    """Docstring for MyClass. """

    def __init__(self, member):
        pass
        self.member = member

    def add(self, arg):
        self.member += arg
        print(self.member)


def event(earg, callback):
    callback(earg)

if __name__ == "__main__":
    mc = MyClass(0)

    event(1, mc.add)
    event(1, mc.add)
    event(1, mc.add)
