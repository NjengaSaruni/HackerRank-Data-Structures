# Given an array, , of  integers, print each element in reverse order as a single line of space-separated integers.
# !/bin/python

import os

# Complete the reverseArray function below.
def reverseArray(a):
    a.reverse()
    
if __name__ == '__main__':
    array = [1, 2, 3, 4]
    reverseArray(array)
    print(array)


