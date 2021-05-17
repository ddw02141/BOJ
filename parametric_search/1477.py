N, M, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(L)
arr.sort()

answer = 1000
left = 0
right = 1000
while left <= right:
    mid = (left + right) // 2
    prevA = 0
    additionalRest = 0
    for a in arr:
        if (a - prevA) % mid == 0:
            additionalRest += ((a - prevA) // mid - 1)
        else:
            additionalRest += (a - prevA) // mid
        prevA = a
    if additionalRest <= M:
        # 정답이 될 수 있음
        # mid를 더 줄여서 확인해 볼 필요도 있음
        answer = min(answer, mid)
        right = mid - 1
    else:
        left = mid + 1

print(answer)
