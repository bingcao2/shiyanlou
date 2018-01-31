#!/usr/bin/env python3

import sys
from collections import namedtuple

Income = namedtuple('Income', ['start', 'tax_rate', 'quick_substractor'])

Income_start = 3500

Income_tax_table = [
    Income(80000, 0.45, 13505),
    Income(55000, 0.35, 5505),
    Income(35000, 0.30, 2755),
    Income(9000, 0.25, 1005),
    Income(4500, 0.20, 555),
    Income(1500, 0.10, 105),
    Income(0, 0.03, 0),
]

Social_Insurance = {
    'a': 0.08,
    'b': 0.02,
    'c': 0.005,
    'd': 0.06
}

def calc_remain(income):
    social = income * sum(Social_Insurance.values())
    income_remain = income - social
    tax = income_remain - Income_start
    if tax <= 0:
        return '0.00', '{:.2f}'.format(income)
    for item in Income_tax_table:
        if tax > item.start:
            tax_final = tax * item.tax_rate - item.quick_substractor
            return '{:.2f}'.format(tax_final), '{:.2f}'.format(income_remain - tax_final)

def main():
    for item in sys.argv[1:]:
        employee_id, income_string = item.split(':')
        try:
            income = int(income_string)
        except ValueError:
            print('Parameter Error')
        _, remain = calc_remain(income)
        print('{}:{}'.format(employee_id, remain))

if __name__ == '__main__':
    main()
