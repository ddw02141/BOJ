DIRECTION = {
    1: (-1, 0),
    2: (1, 0),
    3: (0, 1),
    4: (0, -1),
}


class Shark:
    def __init__(self, s, d, z):
        self.speed = s
        self.direction = DIRECTION[d]
        self.size = z


def moveSharks(matrix):
    newMatrix = [[None for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if matrix[i][j]:
                shark = matrix[i][j]
                newI, newJ = i + shark.direction[0] * shark.speed, j + shark.direction[1] * shark.speed
                xQ, xR = newI // (R - 1), newI % (R - 1)
                yQ, yR = newJ // (C - 1), newJ % (C - 1)
                if newI < 0 or newI >= R:
                    if xQ % 2 == 1:
                        shark.direction = (shark.direction[0] * -1, shark.direction[1] * -1)
                        newI = R - xR - 1
                    else:
                        newI = xR
                elif newJ < 0 or newJ >= C:
                    if yQ % 2 == 1:
                        shark.direction = (shark.direction[0] * -1, shark.direction[1] * -1)
                        newJ = C - yR - 1
                    else:
                        newJ = yR
                if newMatrix[newI][newJ]:
                    if shark.size > newMatrix[newI][newJ].size:
                        newMatrix[newI][newJ] = shark
                else:
                    newMatrix[newI][newJ] = shark
    return newMatrix


def getSharksSize(matrix, sharks):
    answer = 0
    for r, c, s, d, z in sharks:
        matrix[r - 1][c - 1] = Shark(s, d, z)
    for time in range(C):
        for i in range(R):
            if matrix[i][time]:
                answer += matrix[i][time].size
                matrix[i][time] = None
                break
        matrix = moveSharks(matrix)
    return answer


if __name__ == "__main__":
    R, C, M = map(int, input().split())
    MATRIX = [[None for _ in range(C)] for _ in range(R)]
    SHARKS = [list(map(int, input().split())) for _ in range(M)]
    answer = getSharksSize(MATRIX, SHARKS)
    print(answer)
