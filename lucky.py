# -*- coding: utf-8 -*-
import re
"""
Created on Mon Mar 21 12:59:51 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""


def reg_ex_solution(comb: str):
    rule = "(?:5+6|6+5)[56]*"
    combs = re.findall(rule, comb)
    if not combs:
        return 0
    return max(combs, key=len)


def main():
    line = input('series: ')
    print(reg_ex_solution(line))


if __name__ == '__main__':
    main()
