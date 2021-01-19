# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2021-01-19 11:06
@author: Li Luyao
"""


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # if n == 0: return nums1
    # nums1[m:] = nums2[:]
    # return nums1.sort()

    # if n == 0: return nums1
    # nums1[m:] = nums2[:]
    # i = 0
    # while i < (m+n-1):
    #     if nums1[i] <= nums1[i+1]:
    #         i += 1
    #     else:
    #         nums1[i], nums1[i+1] = nums1[i+1], nums1[i]
    #         i = 0
    # return nums1

    # if n == 0: return nums1
    # res = [0] * (m+n)
    # i, j, k = 0, 0, 0
    # while i < m and j < n:
    #     if nums1[i] <= nums2[j]:
    #         res[k] = nums1[i]
    #         i += 1
    #     else:
    #         res[k] = nums2[j]
    #         j += 1
    #     k += 1

    # if i == m: res[k:] = nums2[j:]
    # if j == n: res[k:] = nums1[i:]
    # return res

    if m == 0: return nums2
    if n == 0: return nums1
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[i], nums1[k] = nums1[k], nums1[i]
            i -= 1
        else:
            nums2[j], nums1[k] = nums1[k], nums2[j]
            j -= 1
        k -= 1

    if i == -1: nums1[:j] = nums2[:j]
    return nums1


nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(merge(nums1, m, nums2, n))


