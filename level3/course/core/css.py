# @---wufeng---


import os,sys
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)

from config.logger import log

class Menu(object):
    """
    菜单类
    """

    def __init__(self,menu):
        self.menu = menu
        self.menu_list = []
        self.menu_list.append(self.menu)

    def display_menu(self):
        """
        打印菜单
        :return: 
        """
        dis_template = '\t%d、%s'
        menu_num = 1
        current_menu = self.menu_list[-1]
        current_level = {}
        for key in current_menu:
            print(dis_template %(menu_num,key))
            current_level[str(menu_num)] = key
            menu_num += 1
        else:
            print(dis_template % (0, '退出'))

        return current_level,current_menu

    def select_menu(self):
        """
        选择菜单
        :return: 
        """        current_level,current_menu = self.display_menu()
        exit_flag = False
        while not exit_flag:
            _input = input('输入选择的编码：\n>>')
            if _input == '0':
                if len(self.menu_list) == 1:
                    exit_flag = True
                else:
                    self.menu_list.pop()                                        #删除一级目录
                    return self.select_menu()                                   #递归调用
            elif _input in current_level :
                if isinstance(current_menu[current_level[_input]],str):         #判断value是否是字符串 是则到底 返回
                    return current_menu[current_level[_input]]
                else:
                    self.menu_list.append(current_menu[current_level[_input]])  #添加当前级别目录
                    return self.select_menu()                                   #递归调用 选择当前级别目录
            else:
                print('请输入正确的编码')

class inputfactory(object):
    def __init__(self,keys):
        self.keys = keys

    def get_input(self,input_info):
        _input = input('输入%s'% input_info)
        return _input
    def select_input(self,):
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

    menu = {
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

    a = Menu(menu)
    a.select_menu()


