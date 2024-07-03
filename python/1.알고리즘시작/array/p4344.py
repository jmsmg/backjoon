C = int(input())

for i in range(C):
    a = list(map(int, input().split()))
    everage = 0
    count = 0
    for idx in range(1, len(a)):
        everage += a[idx]
    everage = everage / a[0]

    for j in range(1, len(a)):
        if a[j] > everage:
            count += 1

    count = count / a[0] * 100
    print(str('%.3f' % round(count, 3)) + "%")
