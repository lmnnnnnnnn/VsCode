''' 
@Author: Mengnan Li 
@Date: 2019-10-15 12:59:55 
@Last Modified by: Mengnan Li 
@Last Modified time: 2019-10-15 12:59:55 
'''

import threading
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec):
    print('start nloop', nloop, "st:", ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())

def main():
    print('staring at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()