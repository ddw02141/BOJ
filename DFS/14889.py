import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
my_map = dict()
people = {i: False for i in range(n)}
for i in range(n):
    line = list(map(int, input().split()))
    for j, l in enumerate(line):
        if i not in my_map:
            my_map[i] = dict()
        my_map[i][j] = l

answer = 4000000


def dfs(count, index):
    global answer
    if index == n:
        return
    if count == n // 2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if people[i] and people[j]:
                    start += my_map[i][j]
                elif not people[i] and not people[j]:
                    link += my_map[i][j]
        candi = abs(start - link)
        answer = min(answer, candi)
        return
    people[index] = True
    dfs(count + 1, index + 1)
    people[index] = False
    dfs(count, index + 1)


if __name__ == "__main__":
    dfs(0, 0)
    print(answer)
