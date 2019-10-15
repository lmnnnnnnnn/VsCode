# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@Author: mn.l 
@Date: 2019-10-15 19:36:27
@Last Modified by: mn.l 
@Last Modified time: 2019-10-15 19:36:27 
'''

import threading
from time import ctime

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
    
    def getResult(self):
        return self.res

    def run(self):
        print('starting', self.name, 'at:', ctime())
        self.res = self.func(*self.args)
        print(self.name, 'finished at:', ctime())
