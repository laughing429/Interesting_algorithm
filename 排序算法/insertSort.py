#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Create on: 2018/5/3 0003 10:17 
# Author: Lyu 
# Annotation: 插入排序算法

import numpy as np
import time

def insertSort(numbers):
    result = []
    n = len(numbers)
    for i in range(n):
        inserted = numbers[i]
        if not result:
            result.insert(0, inserted)
            continue
        n_result = len(result)
        for j in range(n_result):
            if inserted < result[j]:
                result.insert(j, inserted)
                break
            if j == n_result-1:
                result.insert(n_result, inserted)
    return result


if __name__ == '__main__':
    start = time.time()
    numbers = np.random.randn(5).tolist()
    print insertSort(numbers)
    print "cost %.4fs" % (float(time.time())-float(start))