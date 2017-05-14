# @---wufeng---


import os,sys
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)

from config.logger import log

log.debug('start ...')