# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:22 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""

# Алгоритм 1. Перебор всіх пар. Складність O(n^2)

def perebor(S, arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j] == S):
                return [arr[i], arr[j]]
    return -1

# Алгоритм 2. Хеш сет. Складність O(n), використання додаткової пам'яті O(n)

def hash_set(S, arr):
    hset = []
    for i in range(len(arr)):
        number_to_find = S - arr[i]
        if number_to_find in hset:
            return [number_to_find, arr[i]]
        hset.append(arr[i])
    return -1

# Алгоритм 3. Бінарний пошук. Складність O(n*log(n))

def bin_search(S, arr):
    for i in range(len(arr)):
        number_to_find = S - arr[i]
        l = i + 1
        r = len(arr) - 1
        while(l <= r):
            mid = l + (r - l)//2
            if (arr[mid] == number_to_find):
                return [arr[i], arr[mid]]
            if (number_to_find < arr[mid]):
                r = mid - 1
            else:
                l = mid + 1
    return -1

# Алгоритм 4. Два вказівники. Складність O(n) - НАЙКРАЩИЙ АЛГОРИТМ!

def two_pointers(S, arr):
    l = 0
    r = len(arr) - 1
    while(l < r):
        suma = arr[l] + arr[r]
        if (suma == S):
            return [arr[l], arr[r]]
        if (suma < S):
            l += 1
        else:
            r -= 1
    return -1

