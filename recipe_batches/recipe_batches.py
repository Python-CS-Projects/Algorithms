#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    total = 0
    notEnough = False
    index = 0
    recipe_len = len(recipe) - 1
    for i in recipe:
        # Check if all the needed ingredients exist
        if i in ingredients:
            if recipe[i] > ingredients[i]:
                print(f"Not enough {i}")
                notEnough = True
            elif index == recipe_len:

                total += 1
            else:
                ingredients[i] -= recipe[i]

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
