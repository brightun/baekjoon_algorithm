n = int(input())
stack = []
op = []
count = 1
check = True

for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        check = False

if check == False:
    print('NO')
else:
    for i in op:
        print(i)
