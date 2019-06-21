#!/usr/bin/env python
# encoding: utf-8
"""
@author: frank
@file: list_example.py
@time: 2019/6/20 9:08
@desc:
"""


# squares = [1, 4, 9, 16, 25]
# print(squares)
# print(squares[-1])
# print(squares[-3:])
# print(squares[:])
# newSquares = squares + [36, 49, 64, 81, 100]
# print(newSquares)
# newSquares.append(4 ** 3)
# print(newSquares)
# newSquares[:] = []
# print(newSquares)

# a, b = 0, 1
# while a < 10:
#     a, b = b, a + b  # 等同于 a=b   b=a+b
#     print(a, b)

# list1 = []
# for i in range(5):
#     list1.append(i)
# print(list1)  # [0, 1, 2, 3, 4]
#
# list2 = []
# for i in range(5, 10):  # 输出5~10
#     list2.append(i)
# print(list2)  # [5, 6, 7, 8, 9]
#
# list3 = []
# for i in range(0, 10, 4):  # 输出10以内数之间间隔4
#     list3.append(i)
# print(list3)  # [0, 4, 8]
#
# list4 = []
# for i in range(-10, -100, -30):
#     list4.append(i)
# print(list4)  # [-10, -40, -70]
#
# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])

# a = input("input:")  # 控制台输入
# print(a)
# print(a in ('y', 'ye', 'yes'))


# print(list(range(3, 6)))
# args = [3, 6]
print(list(range(*args)))


def make_incrementor(n):
    return lambda x: x + n


print(make_incrementor(42))
f = make_incrementor(42)
print(f(0))
