# @---wufeng---


import os,sys
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)

from config.logger import log


admin_level1 = '''
    1、学校管理
    2、班级管理
    3、课程管理
    4、讲师管理
'''

class School(object):
    pass

class Teacher(object):
    pass

class Student(object):
    pass

class Display(object):
    def __init__(self,menu_tital,menu_list):
        self.menu_tital = menu_tital
        self.menu_list = menu_list

    def menu_select(self):
        print(self.menu_tital)
