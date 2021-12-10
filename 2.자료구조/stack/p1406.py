import sys
a = list(sys.stdin.readline().strip())
b = []

N = len(a)
M = int(sys.stdin.readline())

for i in range(M):
    cursor = sys.stdin.readline().strip()

    if cursor[0] == 'L' and a != []:
        b.append(a.pop())
    elif cursor[0] == 'D' and b != []:
        a.append(b.pop())
    elif cursor[0] == 'B' and a != []:
        a.pop()
    elif cursor[0] == 'P':
        a.append(cursor[2])

print(''.join(a+list(reversed(b))))