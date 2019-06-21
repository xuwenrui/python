#!/usr/bin/env python
# encoding: utf-8
"""
@author: frank
@file: chapter1.py
@time: 2019/6/19 9:14
@desc:
"""

# 字符产方法api https://docs.python.org/3/library/stdtypes.html#string-methods

# 如果您不希望将前面提到的字符\解释为特殊字符，则可以通过在第一个引号之前添加原始字符串来使用原始字符串r：
# print(r'C:\some\name')

# 使用"""..."""或'''...''打印多行
# print("""Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
# """)

# 拼接字符串或使用+号
# print('Py' 'thon')  # 仅限两个字符串
# text = ('Put several strings within parentheses '
#         'to have them joined together.')
# print(text)

# word = 'Python Python'
# # print(word[0])
# # print(word[-1])  # 正数从左边算，索引从0开始；负数从右面算，索引从-1开始
# # print(word[1:3])    # 截取字符串
# # print(word[1:]) # 和print(word[1:20])效果是一样的
# # print('Python'[3])
# print(word.count('P', 0, len(word)))    # 统计字符串里某个字符出现的次数


# 使用列表作为堆栈
# stack = [3, 4, 5]
# stack.append(6)
# print(stack.pop())

# 使用列表作为队列
# 也可以使用列表作为队列，其中添加的第一个元素是检索的第一个元素（“先进先出”）;
# 但是，列表不能用于此目的。虽然列表末尾的追加和弹出很快，但是从列表的开头进行插入或弹出是很慢的（因为所有其他元素都必须移动一个）。
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Graham")
print(queue.popleft())