a = []
for i in range(10):
    b = int(input()) % 42
    a.append(b)

print(len(set(a)))