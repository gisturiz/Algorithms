#!/usr/bin/python

import argparse
import sys

# def find_max_profit(prices):

#   min_price = sys.maxsize
#   max_profit = 0

#   for i in range(0, len(prices) - 1):
#     if prices[i] < min_price:
#       min_price = prices[i]
#       print(min_price)
#     elif prices[i] - min_price > max_profit:
#       max_profit = prices[i] - min_price
#       print(max_profit)

#   return max_profit


def find_max_profit(prices):

    largest = max(prices[1:])
    newList = prices[:prices.index(largest)]
    smallest = min(newList)
    result = largest - smallest

    return result


array = [100, 90, 80, 50, 20, 10]

find_max_profit(array)

# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
