if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        if N == 0:
            print("%d %d" % (1, 0))
        elif N == 1:
            print("%d %d" % (0, 1))
        else:
            dp = [0 for _ in range(N + 1)]
            dp[N] = 1
            for i in reversed(range(2, N + 1)):
                dp[i - 1] += dp[i]
                dp[i - 2] += dp[i]
            print("%d %d" % (dp[0], dp[1]))
