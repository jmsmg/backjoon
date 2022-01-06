n = int(input())
A = list(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))

A.sort()

for i in range(m):
    L = 0
    R = m-1
    pivot = (L+R)//2
    
    while L <= R:

