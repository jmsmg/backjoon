import sys
n = int(sys.stdin.readline())
array = []

for i in range(n):
    array.append(sys.stdin.readline())

array = list(set(array))

array.sort()
array.sort(key=lambda x : len(x))

for i in array:
    print(i, end='')
