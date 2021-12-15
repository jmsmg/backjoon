N, K = map(int, input().split())

result = 0
while 1:
    target = (N // K) * K
    result += N - target
    N = target
    if N < K:
        break
    N //= K
    result += 1

result += (N - 1)
print(result)
