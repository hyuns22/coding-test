import sys
T = int(sys.stdin.readline())

stack = []
mx = 0
print_stack = []
for i in range(T):
    num = int(sys.stdin.readline())
    if num > mx:

        for j in range(mx+1, num+1):
            stack.append(j)
            print_stack.append("+")

        stack.pop()
        print_stack.append("-")
        mx = num

    elif num == mx:
        stack.pop()
        print_stack.append("-")


    else:
        if num in stack:
            for j in range(len(stack)-1, -1, -1):
                if stack[j] == num:
                    stack.pop()
                    print_stack.append("-")
                    break

                stack.pop()
                print_stack.append("-")
        else:
            print_stack.append("NO")
            break

if print_stack[-1] == "NO":
    print("NO")
else:
    for i in print_stack:
        print(i)
