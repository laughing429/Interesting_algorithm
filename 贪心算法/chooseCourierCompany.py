#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Create on: 2018-06-13
# Author: Lyu 
# Annotation:贪心算法：对于一些比较复杂的事情，用一些简单的算法并不能很快的解决。这时候往往就需要使用贪心算法，每一步操作都选择局部最优解，往往最终就是全局最优解

"""
    假设这样一个场景：你开了一家网店，由于现在快递公司并不完善，不能送到全国每个省份，你需要对所有的快递公司进行选择，来满足你的要求。并且选择最少的快递公司。
    这个问题看似不难，其实很复杂。如果有N家快递公司，那么全部的组合就是2^n种可能（每一家就有两种情况，选择或者不选择，所有n家就有2^n家。
    那么如果在这个问题下使用贪心算法，就可以这样做：
    1.选择一家覆盖了最多未覆盖省的公司
    2.重复第一步
"""

def greedy():
    province = set(["河北", "山西", "辽宁", "吉林", "黑龙江", "江苏", "浙江", "安徽", "福建", "江西"]) # 需要运算的省份
    company = {} # 每家快递公司能运送的省份
    company["顺丰"] = set(["河北", "山西", "辽宁", "江苏", "浙江"])
    company["圆通"] = set(["吉林", "浙江", "北京"])
    company["中通"] = set(["黑龙江", "江西"])
    company["韵达"] = set(["江苏", "浙江", "江苏"])
    company["EMS"] = set(["浙江", "安徽", "河北", "山西", "上海"])
    company["德邦"] = set(["福建", "江西", "安徽"])

    result = []
    provinceNeed = province
    while provinceNeed:
        provinceCover = set()
        bestCompany = None
        for tempCompany, tempProvince in company.items():
            cover = province & tempProvince
            if len(cover) > len(provinceCover):
                provinceCover = cover
                bestCompany = tempCompany
        provinceNeed -= provinceCover
        result.append(bestCompany)

    return result

if __name__ == '__main__':
    print '/'.join(greedy())
