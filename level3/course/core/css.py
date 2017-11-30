# @---wufeng---

from core.config import *

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
    def __init__(self,id,school_name,school_area):
        self.id = id
        self.school_name = school_name
        self.school_area = school_area




class Classes(object):
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



