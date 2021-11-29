n = int(input())

a = list(map(int, input().split()))
b = 0
m = max(a)

for i in range(n):
    b += a[i]/m*100

print(b/n)