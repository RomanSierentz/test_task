# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:22 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""


def get_pair(nums: list, s: int) -> tuple:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    i = 0
    j = len(nums) - 1
    while nums[i] != nums[j]:
        if nums[i] + nums[j] == s:
            return nums[i], nums[j]
        if nums[i] + nums[j] < s:
            i += 1
            continue
        j -= 1
    return 0, 0


def main():
    s = int(input('S: '))
    arr = input('Nums, coma separated: ')
    nums = list(map(int, arr.split(',')))
    print(get_pair(nums, s))


if __name__ == '__main__':
    main()
