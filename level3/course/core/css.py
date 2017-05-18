# @---wufeng---


import os,sys
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)

from config.logger import log


menu = {
    '后台管理':{
        '学校管理':{
            "查看学校":None,
            "添加学校":None,
            "删除学校":None
        },
        '班级管理':{
            "查看班级": None,
            "添加班级": None,
            "删除班级": None
        },
        '课程管理':{
            "查看课程": None,
            "添加课程": None,
            "删除课程": None
        },
        '讲师管理':{
            "查看讲师": None,
            "添加讲师": None,
            "删除讲师": None
        }
    },
    '讲师':{
        '管理班级':None,
        '选择上课班级':None,
        '查看班级学员列表':None,
        '修改学员成绩':None
    },
    '学员':{
        '注册':None,
        '交学费':None,
        '选择班级':None
    }
}

class School(object):
    pass

class Teacher(object):
    pass

class Student(object):
    pass

class Display(object):

    def __init__(self,menu):
        self.menu = menu
        self.menu_list = []
        self.menu_list.append(self.menu)

    def print_menu(self):
        dis_template = '\t%d、%s'
        menu_num = 1
        current_menu = {}
        print_menu = self.menu
        if len(self.menu_list) > 0 :
            for i in self.menu_list:
                print_menu = print_menu[i]
        for key in print_menu:
            print(dis_template %(menu_num,key))
            current_menu[str(menu_num)] = key
            menu_num += 1
        return current_menu

    def select_menu(self):
        current_menu = self.print_menu()
        exit_flag = False
        while not exit_flag:
            _input = input('输入选择的编码：\n>>')
            if _input == 'q':
                exit_flag = True
            elif _input in current_menu :
                self.menu_list.append(current_menu[_input])
                if
            else:
                print('请输入正确的编码')

a = Display(menu)
a.select_menu()



