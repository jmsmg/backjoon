import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

stack = []

for i in range(n):
    j = i+1
    while j < len(a):
        if a[i] < a[j]:
            stack.append(a[j])
            break
        elif a[i] >= a[j] and j == len(a)-1:
            stack.append(-1)
        j += 1
    if i == len(a)-1:
        stack.append(-1)

print(*stack)
