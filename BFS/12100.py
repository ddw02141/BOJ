def left(mat):
    newMat = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        target = [num for num in mat[i]]
        isMerged = [False for _ in range(N)]
        prev = -1
        idx = 0
        while idx < len(target):
            if target[idx] == 0:
                del target[idx]
            elif target[idx] == prev and not isMerged[idx - 1]:
                isMerged[idx - 1] = True
                target[idx - 1] += target[idx]
                prev = target[idx - 1]
                del target[idx]
            else:
                prev = target[idx]
                idx += 1
        while len(target) < N:
            target.append(0)
        newMat[i] = target
    return newMat


def right(mat):
    reversedMat = reverse(mat)
    return reverse(left(reversedMat))


def up(mat):
    invertedMat = invert(mat)
    return invert(left(invertedMat))


def down(mat):
    invertedAndReversed = invertAndReverse(mat)
    return reverseAndInvert(left(invertedAndReversed))


def invert(mat):
    return list(list(row) for row in zip(*mat))


def reverse(mat):
    return [row[::-1] for row in mat]


def invertAndReverse(mat):
    inverted = invert(mat)
    return reverse(inverted)


def reverseAndInvert(mat):
    reversed = reverse(mat)
    return invert(reversed)


def printMat(mat):
    for row in mat:
        print(row)


def findMax(mat):
    maxi = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] > maxi:
                maxi = mat[i][j]
    return maxi


if __name__ == "__main__":
    global N
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # printMat(left(matrix))
    # printMat(right(matrix))
    # printMat(up(matrix))
    # printMat(down(matrix))

    answer = 0
    q = [[matrix, 0]]
    while q:
        current, trial = q.pop(0)
        if trial == 5:
            answer = max(answer, findMax(current))
            continue
        for op in (left, right, up, down):
            newCurrent = op(current)
            q.append([newCurrent, trial + 1])
    print(answer)
