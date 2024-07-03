import sys
q, l = map(int, sys.stdin.readline().split())

q = list(range(1, q+1))
answer = []
idx = 0

for i in range(len(q)):
    idx += l-1

    if idx >= len(q):
        idx = idx % len(q)

    answer.append(q.pop(idx))

b = ', '.join(map(str, answer))
print(f'<{b}>')