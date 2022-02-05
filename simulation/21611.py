import sys

input = sys.stdin.readline

DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIRECTION_TO_FUNCTION = {
    0: (lambda minX: minX + 1),
    1: (lambda maxY: maxY - 1),
    2: (lambda maxX: maxX - 1),
    3: (lambda minY: minY + 1),
}
BLIZZARD_DIRECTION = [None, (-1, 0), (1, 0), (0, -1), (0, 1)]


def init(n):
    idxToGrid = dict()
    gridToIdx = dict()
    dirIdx = 0
    grid = (0, 0)
    minX = minY = 0
    maxX = maxY = n - 1
    directionToMinMax = [minX, maxY, maxX, minY]
    for idx in reversed(range(1, n * n)):
        idxToGrid[idx] = grid
        gridToIdx[grid] = idx
        direction = DIRECTION[dirIdx]
        newGrid = (grid[0] + direction[0], grid[1] + direction[1])
        if newGrid[0] < directionToMinMax[0] or newGrid[0] > directionToMinMax[2] \
                or newGrid[1] < directionToMinMax[3] or newGrid[1] > directionToMinMax[1]:
            directionToMinMax[dirIdx] = DIRECTION_TO_FUNCTION[dirIdx](directionToMinMax[dirIdx])
            dirIdx = (dirIdx + 1) % 4
            direction = DIRECTION[dirIdx]
            newGrid = (grid[0] + direction[0], grid[1] + direction[1])
        grid = newGrid
    return idxToGrid, gridToIdx


def explode(current):
    canExplode = False
    prevM = current[0]
    m = current[0]
    count = 1
    mAndCount = list()
    for cur in current[1:]:
        if cur == m:
            count += 1
        else:
            if count >= 4:
                exploded[m] += count
                if prevM == cur:
                    canExplode = True
            else:
                mAndCount.append((m, count))
            prevM = m
            m = cur
            count = 1
    if count >= 4:
        exploded[m] += count
    else:
        mAndCount.append((m, count))

    newCurrent = list()
    for m, count in mAndCount:
        for _ in range(count):
            newCurrent.append(m)

    return newCurrent, canExplode


def refactor(current, n):
    if len(current) <= 1:
        return current

    m = current[0]
    count = 1
    newCurrent = list()
    for cur in current[1:]:
        if cur == m:
            count += 1
        else:
            if m == -1:
                newCurrent.append(m)
            else:
                newCurrent.append(count)
                newCurrent.append(m)
            m = cur
            count = 1
    newCurrent.append(count)
    newCurrent.append(m)

    return newCurrent[:n * n]


if __name__ == "__main__":
    N, M = map(int, input().split())
    idxToGrid, gridToIdx = init(N)
    # for idx in reversed(range(1, N * N)):
    #     print("idx:", idx, "grid:", idxToGrid[idx])
    current = [-1]
    exploded = [None, 0, 0, 0]

    matrix = [list(map(int, input().split())) for _ in range(N)]

    for idx in range(1, N * N):
        grid = idxToGrid[idx]
        marble = matrix[grid[0]][grid[1]]
        if marble == 0:
            break
        current.append(marble)
    # print("Initial current")
    # print(current)
    shark = (N // 2, N // 2)

    dss = [list(map(int, input().split())) for _ in range(M)]

    for D, S in dss:
        # Stage 1
        bd = BLIZZARD_DIRECTION[D]
        gridToDestroy = (N // 2, N // 2)
        for i in range(S):
            gridToDestroy = (gridToDestroy[0] + bd[0], gridToDestroy[1] + bd[1])
            idxToDestroy = gridToIdx[gridToDestroy]
            if idxToDestroy >= len(current):
                continue
            current[idxToDestroy] = 0
        # print("Stage 1 current")
        # print(current)
        # Stage 2
        current = [cur for cur in current if cur != 0]

        # print("Stage 2 current")
        # print(current)
        # Stage 3
        while True:
            current, isExploded = explode(current)
            if not isExploded:
                break
        #     # print("Stage 3 current")
        #     # print(current)
        #     # print("exploded")
        #     # print(exploded)
        #
        # Stage 4
        current = refactor(current, N)
    #     # print("Stage 4 current")
    #     # print(current)
    #
    print(sum([i * exploded[i] for i in range(1, 3 + 1)]))
