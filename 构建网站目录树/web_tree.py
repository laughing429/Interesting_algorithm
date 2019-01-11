#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Create on: 2018-12-25
# Author: Lyu 
# Annotation:


class Tree(object):
    def __init__(self, init_tree, nodes):
        self.init = init_tree
        self.child = None
        self.nodes = nodes


    def insert(self, node):
        self.child = self.child.setdefault(node, {})


    def main(self):
        for i in range(len(self.nodes)):
            if i == 0:
                self.child = self.init.setdefault(self.nodes[i], {})
            else:
                self.insert(self.nodes[i])

        return self.init


if __name__ == '__main__':
    url1 = 'www.sc.gov.cn/10462/wza2012/jgzn/jgzn.shtml'
    url2 = 'www.sc.gov.cn/10462/10464/10757/10868/2018/4/17/10449166.shtml'
    url3 = 'www.sc.gov.cn/10462/10580/10583/zdxm.shtml'
    url4 = 'www.sc.gov.cn/10462/10464/10757/2018/12/24/e0ba5e9e651943c5b859e7ec3460e19f.shtml'
    url5 = 'www.sc.gov.cn/zcwj/xxgk/NewT.aspx?i=20181214202318-251449-00-000'
    urls = [url1, url2, url3, url4, url5]
    result = {}
    for url in urls:
        tree = Tree(result, url.split('/'))
        result = tree.main()

    print(result)








