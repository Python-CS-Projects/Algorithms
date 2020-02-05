#!/usr/bin/python

import argparse


def find_max_profit(arr):
    # max profit
    max_profit_so_far = max(arr[1:])
    current_min_price_so_far = 0
    index = 0

    for i in arr:

        if max_profit_so_far == i:
            my_arr = arr[:index]
            current_min_price_so_far = min(my_arr)
            max_profit_so_far -= current_min_price_so_far
        index += 1

    return max_profit_so_far


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
