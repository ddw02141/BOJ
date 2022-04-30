def factorization(x, num):
    exponential = 0
    while x % num == 0:
        exponential += 1
        x //= num
    return exponential


if __name__ == "__main__":
    N = int(input())
    fac2 = fac5 = 0
    for i in range(1, N + 1):
        fac2 += factorization(i, 2)
        fac5 += factorization(i, 5)
    print(min(fac2, fac5))
