import sys
a = [0] * 5
answer = 0
for i in range(5):
   a[i] = int(sys.stdin.readline().rstrip())

for i in range(5):
    if a[i] < 40:
        answer += 40
    else:
        answer += a[i]

print(answer//5)