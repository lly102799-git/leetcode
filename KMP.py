# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2021/1/17 11:28
Author: Li Luyao
"""
# def KMP(mainStr, patStr):
#     pmt = getPMT(patStr)
#
#     m = len(main_str)
#     p = len(pat_str)
#     i, j = 0, 0
#     while (i < m) and (j < p):
#         if mainStr[i] == patStr[j]:
#             i += 1
#             j += 1
#         elif j != 0:
#             j = pmt[j-1]
#         else:
#             i += 1
#
#     if j == len(patStr):
#         return i - j
#     else:
#         return -1
#
# def getPMT(patStr):
#     pmt = [0] * len(patStr)
#
#     i, j = 0, 1
#     while j < len(patStr):
#         if patStr[i] != patStr[j]:
#             if i == 0: # 该字符串首位字符不相同，pmt值一定为0（前后缀无交集）
#                 pmt[j] = 0
#                 j += 1
#             else:
#                 i = pmt[i-1]
#         else:
#             pmt[j] = i + 1
#             i += 1
#             j += 1
#
#     return pmt
#
# 暴力解法
def str_compare(main_str, pat_str):
    i, j = 0, 0
    res = 0
    while i < len(main_str) and j < len(pat_str):
        if main_str[i] == pat_str[j]:
            i += 1
            j += 1
        else:
            if main_str[i] != pat_str[0]:
                res = i + 1
            else:
                res += 1
            i = res
            j = 0

    if j == len(pat_str):
        return res
    else:
        return -1

def get_pmt(pat_str):
    pmt = [0] * len(pat_str)
    i, j = 0, 1

    while j < len(pat_str):
        if pat_str[i] == pat_str[j]:
            pmt[j] = i + 1
            i += 1
            j += 1
        else:
            if i == 0:
                pmt[j] = 0
                j += 1
            else:
                i = pmt[i-1]
    return pmt


def KMP(main_str, pat_str):
    pmt = get_pmt(pat_str)

    i, j = 0, 0
    while i < len(main_str) and j < len(pat_str):
        if main_str[i] == pat_str[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = pmt[j-1]

    if j == len(pat_str):
        return i - j
    else:
        return -1


if __name__ == '__main__':
    main_str = "abcgbabcabgach"
    pat_str = "abcabgac"

    print(KMP(main_str, pat_str))
    print(str_compare(main_str, pat_str))
    print(main_str.index(pat_str))