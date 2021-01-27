import sys


def push(x):
    queue.append(x)


def pop():
    if(not queue):
        return -1
    else:
        return queue.pop()


def size():
    return len(queue)


def empty():
    return 0 if queue else 1


def front():
    return queue[0] if queue else -1


def back():
    return queue[-1] if queue else -1


N = int(sys.stdin.readline().rstrip())
queue = []

for _ in range(N):
    input_split = sys.stdin.readline().rstrip().split()

    order = input_split[0]

    if order == "push":
        push(input_split[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "front":
        print(front())
    elif order == "back":
        print(back())