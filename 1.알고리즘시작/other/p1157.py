a = input().upper()
b = list(set(a))

array = []
for i in b:
    array.append(a.count(i))

if array.count(max(array)) > 1:
    print('?')
else:
    print(b[array.index(max(array))])
