N = int(input())
M = list(map(str, input().split()))

row = 1
column = 1

for i in range(len(M)):
  if M[i] == 'L' and column != 1:
    column -= 1
  elif M[i] == 'R' and column != N:
    column += 1
  elif M[i] == 'U' and row != 1:
    row -= 1
  elif M[i] == 'D' and row != N:
    row += 1
  
print(row, column, end=' ')