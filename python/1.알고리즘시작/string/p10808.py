S = input()
array = [0] * 26

for i in S:
    array[ord(i) - 97] += 1

for i in array:
    print(i, end=' ')