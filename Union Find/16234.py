from collections import defaultdict

ROWCOL = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def getIdx(r, c):
    return r * N + c


def getCoordinate(idx):
    return idx // N, idx - (idx // N) * N


def find(idx, parent):
    if parent[idx] != idx:
        parent[idx] = find(parent[idx], parent)

    return parent[idx]


def union(idx1, idx2, parent, rank):
    root1 = find(idx1, parent)
    root2 = find(idx2, parent)
    if root1 != root2:
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        else:  # rank[root2] < rank[root1]
            parent[root2] = root1
            if rank[root1] == rank[root2]:
                rank[root1] += 1


def getNumberOfDaysMoving():
    numberOfDaysMoving = 0
    numIndices = N * N
    while True:
        parent = list()
        rank = list()
        for i in range(numIndices):
            parent.append(i)
            rank.append(0)
        for i in range(N):
            for j in range(N):
                for row, col in ROWCOL:
                    newI, newJ = i + row, j + col
                    if newI < 0 or newI >= N or newJ < 0 or newJ >= N:
                        continue
                    diff = abs(MATRIX[i][j] - MATRIX[newI][newJ])
                    if L <= diff <= R:
                        union(getIdx(i, j), getIdx(newI, newJ), parent, rank)
        coordinatesByRoot = defaultdict(list)
        sumByRoot = defaultdict(int)
        for i in range(N):
            for j in range(N):
                root = find(getIdx(i, j), parent)
                coordinatesByRoot[root].append((i, j))
                sumByRoot[root] += MATRIX[i][j]
        if len(coordinatesByRoot) == numIndices:
            break
        for root, coordinates in coordinatesByRoot.items():
            avg = sumByRoot[root] // len(coordinates)
            for i, j in coordinates:
                MATRIX[i][j] = avg
        numberOfDaysMoving += 1

    return numberOfDaysMoving


if __name__ == "__main__":
    N, L, R = map(int, input().split())
    MATRIX = [list(map(int, input().split())) for _ in range(N)]
    answer = getNumberOfDaysMoving()
    print(answer)
