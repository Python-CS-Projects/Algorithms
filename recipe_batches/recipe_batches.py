#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    total = 0
    index = 0
    notEnough = False
    recipe_len = len(recipe) - 1
    for i in recipe:
        if i in ingredients:
            if recipe[i] > ingredients[i]:
                notEnough = True
                return total
            elif index == recipe_len and notEnough == False:
                total += 1
                return total + recipe_batches(recipe, ingredients)
            else:
                ingredients[i] -= recipe[i]
                # print(ingredients)
        else:
            return total
        index += 1
    return total


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
