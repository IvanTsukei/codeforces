user_input = int(input())

res = 0
for i in range(0, user_input):
    problems = input()
    if problems.count('1') >= 2: res += 1

print(res)