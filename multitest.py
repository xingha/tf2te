# -*- coding:utf-8 -*-
# Author : Mr Zhou
# Date : 2019/09/10

from multiprocessing import Queue, Process
import time


def producter(q,name):
    count  = 0
    while 1:
        food = "this product is {}".format(name)
        print('food', food,'--count:',count)
        count += 1
        time.sleep(1)
        q.put(food)


def cumoser(q):
    count = 0
    while 1:
        time.sleep(6)
        q.get()
        print("pasuesed",count)
        count += 1


def multiddd(q,number):
    # q = Queue(4)
    for i in range(number):
        p = Process(target=cumoser, args=(q,))
        p.start()
        p.join()


if __name__ == "__main__":
    q = Queue(4)
    p0 = Process(target=producter, args=(q,"banana"))
    p0.start()
    # p0.join()
    multiddd(q, 2)
    p0.join()
