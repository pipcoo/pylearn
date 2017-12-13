# -*- coding:utf-8 -*-1
# @---wufeng---
import os,sys

base_dir=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,base_dir)

import core

menu =core.Menu(core.MENU)
menu.select()
s1 = core.School(core.create_uuid,'beijing','beijing')
