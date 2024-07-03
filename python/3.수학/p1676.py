def ft_fato(n):
    t = 1
    for i in range(1, n+1):
        t *= i
    return (t)

n = int(input())
count = 0
a = ft_fato(n)
while a % 10 == 0:
    a //= 10
    count += 1
print(count)