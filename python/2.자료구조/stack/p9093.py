T = int(input())

for i in range(T):
    text = list(input().split())
    for j in text:
        print(j[::-1], end=' ')
