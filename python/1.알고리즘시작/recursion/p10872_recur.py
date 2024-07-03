def ft_recursion(n):
    if (2 <= n):
        return(ft_recursion(n-1) * n)
    elif (n == 0):
        return(1)
    else:
        return(n)

n = int(input())

print(ft_recursion(n))