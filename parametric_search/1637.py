def lteCounts(n):
    count = 0
    for acb in acbs:
        a, c, b = acb
        if a <= n <= c:
            count = count + (n - a) // b + 1
        elif c < n:
            count = count + (c - a) // b + 1
    return count


# N = 20_000
N = int(input())
acbs = []

for _ in range(N):
    acb = list(map(int, input().split()))
    acbs.append(acb)

left = 1
right = 2_147_483_647
answer = float("inf")

if lteCounts(right) % 2 == 0:
    print("NOTHING")
else:
    while left <= right:
        mid = (left + right) // 2
        if lteCounts(mid) % 2 == 1:
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1
    print(answer, lteCounts(answer) - lteCounts(answer - 1))



