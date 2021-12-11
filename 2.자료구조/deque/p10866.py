import sys

def push_front(x):
    deque.insert(0, x)

def push_back(x):
    deque.append(x)

def pop_front():
    if len(deque) == 0:
        print(-1)
    else:
        print(deque.pop(0))

def pop_back():
    if len(deque) == 0:
        print(-1)
    else:
        print(deque.pop())

def size():
    print(len(deque))

def empty():
    if len(deque) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(deque) == 0:
        print(-1)
    else:
        print(deque[0])

def back():
    if len(deque) == 0:
        print(-1)
    else:
        print(deque[-1])

deque = []
num = int(sys.stdin.readline().rstrip())

for i in range(num):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'push_front':
        push_front(cmd[1])
    elif cmd[0] == 'push_back':
        push_back(cmd[1])
    elif cmd[0] == 'pop_front':
        pop_front()
    elif cmd[0] == 'pop_back':
        pop_back()
    elif cmd[0] == 'size':
        size()
    elif cmd[0] == 'empty':
        empty()
    elif cmd[0] == 'front':
        front()
    elif cmd[0] == 'back':
        back()