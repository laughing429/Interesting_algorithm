#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# Create on: 2019-01-11
# Author: Lyu 
# Annotation:

"""
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.
"""

# my solution
def cakes(recipe, available):
    index = 0
    key = None

    if not recipe:
        return 0

    for rec in recipe.keys():
        if rec not in available:
            return 0

        if recipe[rec] /1.0/ available[rec] >= index:
            key = rec
            index = recipe[rec] /1.0/ available[rec]

    return int(available[key] / recipe[key])

# best solution
def cakes(recipe, available):
  return min(available.get(k, 0)/recipe[k] for k in recipe)

if __name__ == '__main__':
    recipe = {'flour': 500, 'eggs': 1, 'sugar': 200}
    available = {'flour': 1200, 'eggs': 5, 'milk': 200, 'sugar': 1200}
    print(cakes(recipe, available))