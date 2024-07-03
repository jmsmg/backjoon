def ft_rec(a, b):
    if a == 0:
        return b
    r = b % a
    return ft_rec(r, a)

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    gcd = ft_rec(a, b)
    print((a // gcd) * (b // gcd) * gcd)