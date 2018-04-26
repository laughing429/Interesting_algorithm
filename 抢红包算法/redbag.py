#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Create on: 2018/4/25 0025 14:18 
# Author: Lyu 
# Annotation:抢红包算法实现

# 如果说每个人抢红包的随机数是剩下金额的随机数，那么每个人抢到红包的均值就不一样。所以下面有两种算法

import random
import numpy as np
from collections import Counter

def doubleMean(totalAmount, peopleNum):
    """
    二倍均值法
    totalAmount: 总的金额
    peopleNum: 抢红包总人数
    """
    useAmount = 0
    testAll = []
    for p in range(peopleNum-1):
        restAmount = totalAmount - useAmount
        restPeople = peopleNum - p
        amount = random.uniform(0.01, restAmount/restPeople*2)
        amount = round(amount, 2)
        print "抢到的金额：", amount
        useAmount += amount
        testAll.append(amount)
    # 最后一个人的红包
    amount = totalAmount - useAmount
    print "抢到的金额：", amount
    testAll.append(amount)
    print "总共抢到的金额数：", sum(testAll)

class cutLine(object):
    """
    线段切割法
    """
    def __init__(self, totalAmount, peopleNum):
        self.totalAmount = totalAmount
        self.peopleNum = peopleNum
        self.cut()

    def repeatHandle(self, cutPoint):
        counter = Counter(cutPoint)
        repeatPoint = filter(lambda x:x[1]>2, counter.items())
        if repeatPoint:
            for repeat in repeatPoint: # 获取第一个重复的值
                repeatValue = repeat[0]
                repeatNum = repeat[1] # 重复的值一共有几个
                repeatIndex = cutPoint.index(repeatValue)
                nextValue = cutPoint[repeatIndex+repeatNum]
                subPoint = np.random.uniform(repeatValue, nextValue, repeatNum -1)
                cutPoint.extend(subPoint)
            newcutPoint = cutPoint.sort()
            self.repeatHandle(newcutPoint)
        else:
            return cutPoint


    def cut(self):
        testAll = []
        cutPoint = np.random.uniform(0.01, self.totalAmount, self.peopleNum-1)
        cutPoint = np.round(cutPoint, decimals=2)
        cutPoint.sort()
        cutPoint = cutPoint.tolist()

        # 处理是否有重复的情况
        cutPoint = self.repeatHandle(cutPoint)

        cutPoint.insert(0, 0)
        cutPoint.insert(self.peopleNum, self.totalAmount)
        for point in np.diff(cutPoint):
            print "抢到的金额：", point
            testAll.append(point)
        print "总共抢到的金额数：", sum(testAll)


if __name__ =='__main__':
    # doubleMean(1000, 10)
    cutLine(1000, 200)

