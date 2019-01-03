# Given an array, , of  integers, print each element in reverse order as a single line of space-separated integers.
# !/bin/python

import os


# Complete the reverseArray function below.
def reverseArray(a):
    a.reverse()


def reverseArray1(a):
    left = 0
    right = len(a) - 1

    while left <= right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1

    return a


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    reverseArray1(array)
    print(array)
