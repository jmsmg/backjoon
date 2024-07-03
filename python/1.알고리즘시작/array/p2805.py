N, M = map(int, input().split())

T = list(map(int, input().split()))

L = 0
R = max(T)

while L <= R:
    cut = (L+R)//2
    
    result = 0
    for i in T:
        if cut < i:
            result += i-cut
    
    if result >= M:
        L = cut + 1
    else:
        R = cut - 1

print(R)
