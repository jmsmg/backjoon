def ft_fibonacci(n):
    if 2 > n:
        return n
    return ft_fibonacci(n-1) + ft_fibonacci(n-2)

n = int(input())

print(ft_fibonacci(n))