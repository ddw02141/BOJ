def getOrder(n, x, y):
    if n == 1:
        return x * 2 + y
    d = 2 ** (n - 1)
    if x < d and y < d:
        return getOrder(n - 1, x, y)
    elif x < d <= y:
        return d * d + getOrder(n - 1, x, y - d)
    elif x >= d > y:
        return 2 * d * d + getOrder(n - 1, x - d, y)
    else:  # x >= d and y >= d
        return 3 * d * d + getOrder(n - 1, x - d, y - d)


if __name__ == "__main__":
    N, r, c = map(int, input().split())
    answer = getOrder(N, r, c)
    print(answer)
