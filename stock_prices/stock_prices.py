#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #takes in a list of stock prices
  current_min_price_so_far = prices[0]
  max_profit_so_far = prices[1]
  #First buy
  #Then sell
  #Return the max profit that can be made from a single buy and sell

  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
