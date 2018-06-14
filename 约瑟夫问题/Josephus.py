#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Create on: 2018-06-13
# Author: Lyu 
# Annotation:

"""
据说著名犹太历史学家 Josephus 有过以下的故事：
    在罗马人占领桥塔帕特后，39个犹太人与 Josephus 及他的朋友躲到一个洞中，
    39个犹太人决定宁愿死也不要被敌人抓到，于是决定了一个自杀方式，41个人排成一个圆圈，
    由第1个人开始报数，每报数到第3人该人就必须自杀，然后再由下一个重新报数，
    直到所有人都自杀身亡为止。然而 Josephus 和他的朋友并不想自杀，
    问他俩安排的哪两个位置可以逃过这场死亡游戏？
"""

from collections import deque

def ysf(a, b):
    """
    利用数列旋转实现
    a: 代表队列的长度
    b：代表报数人是多少时出列
    """
    d = deque(range(1, a+1))
    while d:
        d.rotate(-b)
        d.pop()
        if len(d) == 2:
            break
    return d


if __name__ == '__main__':
    print ysf(41, 3)