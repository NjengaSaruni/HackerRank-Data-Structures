def leftRotate(a, r):
    l = len(a)
    r = r % l
    i = r

    if r * 2 > l:
        while i > 0:
            j = (l - r + i) % l
            a[i], a[j] = a[j], a[i]
            i -= 1
    else:
        while i < l:
            j = (l - r + i) % l
            a[i], a[j] = a[j], a[i]
            i += 1


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    leftRotate(a, 3)
    print(a)
