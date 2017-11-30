# @---wufeng---

import time,logging
from run import base_dir


LOGFILE = "%s/logs/css.log" % base_dir  # 日志文件名称
LOGLEVEL = "DEBUG"  # 日志级别
NOW = time.strftime('%Y-%m-%d %H:%M:%S')  # 当前时间格式
DBFILE = "%s/data/css.dat" % base_dir

logging.basicConfig(filename=LOGFILE,  # 日志记录 模块配置
                    format='[%(asctime)s] %(levelname)s: %(message)s',
                    level=LOGLEVEL)
log = logging

MENU = {
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
