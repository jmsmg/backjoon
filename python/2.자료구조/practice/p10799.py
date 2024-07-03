a = list(input())

stack = []
count = 0

for i in range(len(a)):
    if a[i] == '(':
        stack.append('(')
    else:
        if a[i-1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
print(count)
