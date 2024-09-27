"""
Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.
"""

# NOTE: Solution
# - We can build the answer array ans one element at a time. Start two pointers at the first index of each array, and compare their elements. At each iteration, we have 2 values. Whichever value is lower needs to come first in the answer, so add it to the answer and move the respective pointer.

from typing import List


def mergeSortedArrays(arr1: List[int], arr2: List[int])-> List[int]:
    ans = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i < len(arr1):
        ans.append(arr1[i])

    while j < len(arr2):
        ans.append(arr2[j])

    return ans

