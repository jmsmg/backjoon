num = int(input())

for i in range(num):
    a = list(input())
    b = 0
    for j in a:
        if j == '(':
            b += 1
        elif j == ')':
            b -= 1

        if b < 0:
            print('NO')
            break
    if b == 0:
        print('YES')
    elif b > 0:
        print('NO')

