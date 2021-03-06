# -*- coding:utf-8 -*-1
# @---wufeng---


from core import log

class Menu(object):
    """
    菜单类
    """

    def __init__(self,menu):
        self.menu = menu
        self.menu_list = []
        self.menu_list.append(self.menu)

    def display(self):
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

    def select(self):
        """
        选择菜单
        :return: 
        """
        current_level,current_menu = self.display()
        exit_flag = False
        while not exit_flag:
            _input = input('输入选择的编码：\n>>')

            if _input == '0':
                log.info('退出菜单' )
                if len(self.menu_list) == 1:
                    exit_flag = True
                else:
                    self.menu_list.pop()                                        #删除一级目录
                    return self.select()                                   #递归调用
            elif _input in current_level :
                log.info('选择菜单：%s'% current_level[_input])
                if isinstance(current_menu[current_level[_input]],str):         #判断value是否是字符串 是则到底 返回
                    return current_menu[current_level[_input]]
                else:
                    self.menu_list.append(current_menu[current_level[_input]])  #添加当前级别目录
                    return self.select()                                   #递归调用 选择当前级别目录
            else:
                print("""您输入编号不存在。请输入正确的编号！~\n""")
                log.warn('输入编号错误 %s' %_input)
                return self.select()
