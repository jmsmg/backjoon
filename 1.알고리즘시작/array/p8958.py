n = int(input())

for i in range(n):
    a = input()
    s = list(a)
    c = 0
    result = 0

    for j in s:
        if j == 'O':
            c += 1
            result += c
        else:
            c = 0
    print(result)
