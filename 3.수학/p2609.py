def ft_recur(a, b):
    r = a % b
    if r == 0:
        return (b)
    else:
        return ft_recur(b, r)
a, b = map(int, input().split())

print(ft_recur(a, b))
print(int((a * b)/ft_recur(a, b)))
