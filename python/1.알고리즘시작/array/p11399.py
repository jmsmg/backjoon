n = int(input())

array = list(map(int, input().split()))

array.sort()
answer = 0
for i in array:
    answer += i * n
    n -= 1
print(answer)
