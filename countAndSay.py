# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2021/1/18 23:54
Author: Li Luyao
"""

def countAndSay(n):
    if n == 1: return "1"

    res = "1"
    for _ in range(n-1):
        i, temp = 0, ""
        for j, ch in enumerate(res):
            if res[i] != res[j]:
                temp += str(j-i) + res[i]
                i = j
        temp += str(j+1-i) + res[i]
        res = temp

    return res

print(countAndSay(4))