import sys

S = list(sys.stdin.readline().rstrip())
i = 0

while i < len(S):
    if S[i] == '<':
        while S[i] != '>':
            print(''.join(map(str, S[i])), end='')
            i += 1
    elif S[i] == ' ':
        print(' ', end ='')
        i += 1
    else:
        stack = []
        while i < len(S) and S[i].isalnum():
            stack.append(S[i])
            i += 1

        if stack != []:
            print(''.join(map(str, stack[::-1])), end='')
        else:
            print(''.join(map(str, S[i])), end='')
            i += 1

