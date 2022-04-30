from enum import Enum

DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Status(Enum):
    RED_GOAL = 1
    BLUE_GOAL = 2
    NO_GOAL = 3


class Relation(Enum):
    NEVER_OVERLAP = 1
    RED_AHEAD = 2
    BLUE_AHEAD = 3


def tilt(r, b, direction):
    rx, ry = r
    bx, by = b
    redMovable = blueMovable = True
    relation = getRelation(rx, ry, bx, by, direction)
    while redMovable or blueMovable:
        if redMovable and blueMovable:
            rx += direction[0]
            ry += direction[1]
            bx += direction[0]
            by += direction[1]
        elif redMovable:
            rx += direction[0]
            ry += direction[1]
        elif blueMovable:
            bx += direction[0]
            by += direction[1]
        redMovable = isMovable(rx, ry)
        blueMovable = isMovable(bx, by)

    if isInMatrix(bx, by) and matrix[bx][by] == 'O':
        return rx, ry, bx, by, Status.BLUE_GOAL
    elif isInMatrix(rx, ry) and matrix[rx][ry] == 'O':
        return rx, ry, bx, by, Status.RED_GOAL
    if relation == Relation.NEVER_OVERLAP:
        return rx - direction[0], ry - direction[1], bx - direction[0], by - direction[1], Status.NO_GOAL
    elif relation == Relation.RED_AHEAD:
        return rx - direction[0], ry - direction[1], bx - direction[0] * 2, by - direction[1] * 2, Status.NO_GOAL
    elif relation == Relation.BLUE_AHEAD:
        return rx - direction[0] * 2, ry - direction[1] * 2, bx - direction[0], by - direction[1], Status.NO_GOAL


def getRelation(rx, ry, bx, by, direction):
    if direction[0] != 0:
        if ry == by:
            if betweenXClean(rx, bx, ry):
                if (rx - bx) / direction[0] > 0:
                    return Relation.RED_AHEAD
                return Relation.BLUE_AHEAD
    else:
        if rx == bx:
            if betweenYClean(ry, by, rx):
                if (ry - by) / direction[1] > 0:
                    return Relation.RED_AHEAD
                return Relation.BLUE_AHEAD
    return Relation.NEVER_OVERLAP


def betweenXClean(rx, bx, y):
    for x in range(min(rx, bx) + 1, max(rx, bx)):
        if matrix[x][y] == '#':
            return False
    return True


def betweenYClean(ry, by, x):
    for y in range(min(ry, by) + 1, max(ry, by)):
        if matrix[x][y] == '#':
            return False
    return True


def isMovable(x, y):
    return isInMatrix(x, y) and matrix[x][y] == '.' and matrix[x][y] != 'O'


def isInMatrix(x, y):
    return 0 <= x < N and 0 <= y < M


if __name__ == "__main__":
    global N, M, matrix
    global visited
    N, M = map(int, input().split())
    matrix = [list(list(input())) for _ in range(N)]
    visited = set()
    red = blue = hole = None
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'R':
                red = (i, j)
                matrix[i][j] = '.'
            elif matrix[i][j] == 'B':
                blue = (i, j)
                matrix[i][j] = '.'
            elif matrix[i][j] == 'O':
                hole = (i, j)
    # (red, blue, trial)
    q = [[red, blue, 0]]
    isGoal = Status.NO_GOAL
    while q:
        r, b, trial = q.pop(0)
        if (r, b) in visited:
            continue
        visited.add((r, b))
        if trial >= 10:
            break
        for direction in DIRECTION:
            newRx, newRy, newBx, newBy, isGoal = tilt(r, b, direction)
            if isGoal == Status.BLUE_GOAL:
                continue
            elif isGoal == Status.RED_GOAL:
                print(trial + 1)
                break
            else:
                q.append([(newRx, newRy), (newBx, newBy), trial + 1])
        if isGoal == Status.RED_GOAL:
            break

    if isGoal != Status.RED_GOAL:
        print(-1)
