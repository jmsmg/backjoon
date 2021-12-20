def ft_isprime(p):
    if 1 >= p:
        return False
    else:
        for i in range(2, p):
            if p % i == 0:
                return False
        return True

n = int(input())
array = list(map(int, input().split()))

result = 0

for i in array:
    if ft_isprime(i):
        result += 1
print(result)
