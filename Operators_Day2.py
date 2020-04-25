#!/bin/python3

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    x=round(meal_cost+(meal_cost*(tip_percent/100))+(meal_cost*(tax_percent/100)))
    print(x)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
