import sys
a = list(sys.stdin.readline())

i = 0
j = 0
count = 0

while i < len(a):
    if a[i] == '(':
        if a[i-1] == '(':
            j += 1
    else:
        if a[i] == ')':
            if a[i-1] == ')':
                j -= 1
            count += j
    i += 1
print(count)
