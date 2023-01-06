x = sorted('Timur')
user_input = int(input())

for i in range(0, user_input):
    n = input()
    name = input()
    name_check = sorted(name)
    if x == name_check:
        print('YES')
    else:
        print('NO')