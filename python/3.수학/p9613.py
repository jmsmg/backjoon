def ft_rec(a, b):
    if b == 0:
        return a
    else:
        return ft_rec(b, a%b)
    
t = int(input())

for _ in range(t):
    count = 0
    array = list(map(int, input().split()))
    n = array.pop(0)
    for i in range(n):
        for j in range(n):
            if i < j:
                count += ft_rec(array[j], array[i])
    print(count)