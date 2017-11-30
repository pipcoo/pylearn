# -*- coding:utf-8 -*-1
# @---wufeng---
import os,sys

base_dir=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,base_dir)

if __name__ == '__main__':
    try:
        from core import menu
        menu.select()
    except (ImportError) as e:
        print(e)
        exit(1)


