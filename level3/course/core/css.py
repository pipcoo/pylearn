# @---wufeng---
import os,sys
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)
from config.logger import log
from core.module import menu

class inputfactory(object):
    def __init__(self,keys):
        self.keys = keys

    def get_input(self,input_info):
        _input = input('输入%s'% input_info)
        return _input
    def select_input(self,):
        pass



class School(object):
    """
    学校类
    """
    def __init__(self,school_name,school_area):
        self.school_name = school_name
        self.school_area = school_area


class Classes(School):
    """
    班级类
    """
    def __init__(self,school_name,school_area,class_name):
        super().__init__(school_name,school_area)
        self.class_name = class_name


class Course(object):
    """
    课程类
    """
    pass

class SchoolPeople(object):
    """
    学校的人类
    """
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Teacher(SchoolPeople):
    """
    老师类
    """
    def __init__(self,name,age):
        super().__init__(name,age)

class Student(SchoolPeople):
    """
    学生类
    """
    def __init__(self,name,age):
        super().__init__(name,age)


class LearnRecord(object):
    """
    学习记录
    """
    pass

class teachRecord(object):
    """
    教学记录
    """
    pass

class SchoolFactory(object):

    @staticmethod
    def create_shcool(self):
        pass


class Administrator(object):
    """
    管理员
    """
    def create(self):
        pass

    def view(self):
        pass

    def modify(self):
        pass

    def delete(self):
        pass


if __name__ == '__main__':

    menu_info = {
        '后台管理': {
            '学校管理': {
                "查看学校": '',
                "添加学校": '',
                "删除学校": ''
            },
            '班级管理': {
                "查看班级": '',
                "添加班级": '',
                "删除班级": ''
            },
            '课程管理': {
                "查看课程": '',
                "添加课程": '',
                "删除课程": ''
            },
            '讲师管理': {
                "查看讲师": '',
                "添加讲师": '',
                "删除讲师": ''
            }
        },
        '讲师': {
            '管理班级': '',
            '选择上课班级': '',
            '查看班级学员列表': '',
            '修改学员成绩': ''
        },
        '学员': {
            '注册': '',
            '交学费': '',
            '选择班级': ''
        }
    }

    a = menu.Menu(menu_info)
    a.select_menu()


