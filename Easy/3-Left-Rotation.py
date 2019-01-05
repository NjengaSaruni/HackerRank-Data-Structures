def leftRotate(a, r):
    for i in range(r):
        a.append(a.pop(0))


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    leftRotate(a, 3)

    for i in a:
        print(i, end=" ")
