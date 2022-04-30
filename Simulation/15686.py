"""
치킨 집의 갯수 = c
m <= c <= 13
최대 경우의 수 = 13C6 = 1716
집의 개수 = h <= 100
O(100 * 13 * 1716) = 2_230_800
"""


def dfs(idx, count1, r, l, combis):
    if count1 == r:
        combis.append([row for row in l])
        return
    if idx >= len(l):
        return
    # Include idx
    l[idx] = True
    dfs(idx + 1, count1 + 1, r, l, combis)
    l[idx] = False
    # Exclude idx
    dfs(idx + 1, count1, r, l, combis)


def getCombis(n, r):
    combis = list()
    dfs(0, 0, r, [False for _ in range(n)], combis)

    return combis


def getDistance(h, c):
    return abs(h[0] - c[0]) + abs(h[1] - c[1])


def minimumChickenDistance(n, m, matrix):
    home = list()
    chicken = list()
    mcd = float("inf")
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                home.append((i, j))
            elif matrix[i][j] == 2:
                chicken.append((i, j))
    combis = getCombis(len(chicken), m)
    for combi in combis:
        survivedChicken = [c for i, c in enumerate(chicken) if combi[i]]
        cd = 0
        for h in home:
            cdForh = float("inf")
            for c in survivedChicken:
                cdForh = min(cdForh, getDistance(h, c))
            cd += cdForh
        mcd = min(mcd, cd)

    return mcd


if __name__ == "__main__":
    N, M = map(int, input().split())
    MATRIX = [list(map(int, input().split())) for _ in range(N)]
    answer = minimumChickenDistance(N, M, MATRIX)
    print(answer)
