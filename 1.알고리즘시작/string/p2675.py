T = int(input())

for _ in range(T):
    S = list(input().split())
    for i in S[1]:
        print(i*int(S[0]), end='')
    print()
