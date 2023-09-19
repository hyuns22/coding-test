import sys

T = int(input())

for i in range(T):
    stack = []
    li = list(sys.stdin.readline().rstrip())

    t_f = True
    for j in li:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack)==0:
                print("NO")
                t_f = False
                break
            else:
                stack.pop()

    if len(stack)==0 and t_f == True:
        print("YES")
    elif t_f == True:
        print("NO")