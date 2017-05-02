# -*- coding: utf-8 -*-
import sys,os,logging
from . import setting
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logfile_path = BASE + '/logs/' + setting.LOGFILE
logging.basicConfig(filename=logfile_path,
                    format='[%(asctime)s] %(levelname)s: %(message)s',
                    level=setting.LOGLEVEL)

log = logging
