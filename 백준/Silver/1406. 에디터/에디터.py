import sys
sentence = list(sys.stdin.readline().rstrip())
sentence1 = []
T = int(sys.stdin.readline())
cursor = len(sentence)
for i in range(T):
    command = list(sys.stdin.readline().split())
    if command[0] == "L":
        if sentence:
            sentence1.append(sentence.pop())

    elif command[0] == "D":
        if sentence1:
            sentence.append(sentence1.pop())

    elif command[0] == "B":
        if sentence:
            sentence.pop()

    else:
        sentence.append(command[1])


sentence.extend(reversed(sentence1))

print("".join(sentence))
