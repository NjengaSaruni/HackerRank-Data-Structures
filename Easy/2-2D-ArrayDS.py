import sys


def hourglassSum(arr):
    global_max = - sys.maxsize
    col = 0

    while col < 4:
        row = 0
        while row < 4:
            curmax = 0
            inner_col = col
            while inner_col < col + 3:
                curmax += arr[row][inner_col]
                inner_col += 1
            curmax += arr[row + 1][col + 1]

            inner_col = col
            while inner_col < col + 3:
                curmax += arr[row + 2][inner_col]
                inner_col += 1
            print(curmax)
            if curmax > global_max:
                global_max = curmax

            row += 1

        col += 1

    return global_max


if __name__ == '__main__':
    array = [
        [-1, - 1, 0, -9, - 2, - 2 ],
        [- 2, - 1, - 6, - 8, - 2, - 5],
        [- 1, - 1, - 1, - 2, - 3, - 4],
        [- 1, - 9, - 2, - 4, - 4, - 5],
        [- 7, - 3, - 3, - 2, - 9, - 9],
        [- 1, - 3, - 1, - 2, - 4, - 5]
    ]

    print(hourglassSum(array))
