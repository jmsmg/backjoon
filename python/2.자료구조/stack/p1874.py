num = int(input())
stack = []
answer = []
count = 1
mark = 0

for i in range(num):
  n = int(input())
  
  while count <= n:
    stack.append(count)
    answer.append('+')
    count += 1
  
  if stack[-1] == n:
    stack.pop()
    answer.append('-')
  else:
    print('NO')
    mark = 1
    break

if mark == 0:
  for i in answer:
    print(i)
