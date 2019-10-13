# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
@Author: mn.l 
@Date: 2019-10-13 20:00:27
@Last Modified by: mn.l 
@Last Modified time: 2019-10-13 20:00:27 
'''
from time import sleep, ctime

def loop0():
    print('start loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:', ctime())

def loop1():
    print('start loop1 at:', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())

def main():
    print('starting at:', ctime())
    loop0()
    loop1()
    print('all DONE at:', ctime())

if __name__=='__main__':
    main() 