#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Create on: 2018-06-21
# Author: Lyu 
# Annotation:

import numpy as np


def tv_remote(words):
    # Your code here!
    dictionary = np.array([['a', 'b', 'c', 'd', 'e', '1', '2', '3'],
                           ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],
                           ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
                           ['p', 'q', 'r', 's', 't', '.', '@', '0'],
                           ['u', 'v', 'w', 'x', 'y', 'z', '_', '/'],
                           ['Aa', 'SP', None, None, None, None, None, None]])
    last = np.argwhere(dictionary == 'a')
    step = 0
    label = 0 # Record the case of the previous letter
    for w in words:
        if w.isupper() and not label: # up little down big
            route = np.argwhere(dictionary == 'Aa') - last
            step += np.sum(np.abs(route)) + 1
            last = np.argwhere(dictionary == 'Aa')
            w = w.lower()
            route = np.argwhere(dictionary == w) - last
            step += np.sum(np.abs(route)) + 1
            last = np.argwhere(dictionary == w)
            label = 1

        elif w.isupper() and label: # up big down big
            w = w.lower()
            route = np.argwhere(dictionary == w) - last
            step += np.sum(np.abs(route)) + 1
            last = np.argwhere(dictionary == w)

        elif w.islower() and not label: # up little down little
            route = np.argwhere(dictionary == w) - last
            step += np.sum(np.abs(route)) + 1
            last = np.argwhere(dictionary == w)

        elif w.islower() and label: # up big down little
            route = np.argwhere(dictionary == 'Aa') - last
            step += np.sum(np.abs(route)) + 1
            last = np.argwhere(dictionary == 'Aa')
            route = np.argwhere(dictionary == w) - last
            step += np.sum(np.abs(route)) + 1
            last = np.argwhere(dictionary == w)
            label = 0

        else: # not letter
            route = np.argwhere(dictionary == w) - last
            step += np.sum(np.abs(route)) + 1
            last = np.argwhere(dictionary == w)

        if w == ' ':
            route = np.argwhere(dictionary == 'SP') - last
            step += np.sum(np.abs(route)) + 1
            last = np.argwhere(dictionary == 'SP')

    return step

if __name__ == '__main__':
    print tv_remote('DOES')