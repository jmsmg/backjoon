N = int(input())

K = list(map(int, input().split()))
K.sort(reverse=True)
count = 0
i = 0
while i <= range(N):
    i += K[0]
    count += 1
print(count-1)    
