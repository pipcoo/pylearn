#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@version: 0.1
@author: wufeng
@contact: pipcoo@pipcoo.com
@site: http://www.pipcoo.com
@software: PyCharm
@file: start.py
@time: 2017/4/5 23:38
"""

import os,sys
from core import main

BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE)

main.sqlplus()