#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# Create on: 2018-12-28
# Author: Lyu 
# Annotation:用递归实现阶乘

def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n-1)