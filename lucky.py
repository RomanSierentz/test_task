# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:51 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""

def not_same_digits(seq):          # True якщо число не відноситься до типу 555...555 або 666...666
    n = len(seq)
    return (seq != n*'5') and (seq != n*'6')


def lucky_series(trial):       # trial - int/str
    if (type(trial) == int):
        trial = str(trial)

    series56 = []    # масив послідовностей цифр 5 і 6 підряд
    current_s = ""   # поточний символ
    for digit in trial:
        if digit == '5' or digit == '6':
            current_s += digit
        else:
            if current_s:
                series56.append(current_s)
            current_s = ""
    lucky = []
    for x in series56:     # з масиву послідовностей цифр 5 і 6 вибираємо ті, що не складаються з тільки однакових цифр
        if (not_same_digits(x)):
            lucky.append(x)
    return lucky

lucky = lucky_series(4555432455665334)

print(max(lucky, key=len)) # виводимо найдовший lucky series