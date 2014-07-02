#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright notice
# ----------------
#
# Copyright (C) 2013-2014 Daniel Jung
# Contact: djungbremen@gmail.com
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA.
#
"""Implement dummies.

Dummies can have many practical uses, for example if several functions can be
chosen for a certain task (just think of filter functions), or if a function or
class of a third party module is not available. To not have to implement
dummies over and over again (how ever short they are), I wrote this collection
of dummy Python objects."""
__created__ = '2013-07-13'
__modified__ = '2013-07-24'


def function(*args, **kwargs):
    """Dummy function, returning None."""
    return


def function1(x, *args, **kwargs):
    """Dummy function, passing through the first argument."""
    return x


class Class(object):
    """Dummy class."""
    def __init__(self, *args, **kwargs):
        pass


class Decorator(Class):
    """Dummy decorator, the function stays untouched."""
    def __call__(self, func, *args, **kwargs):
        return func
