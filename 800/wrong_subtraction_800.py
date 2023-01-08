user_input = input()
start, decrease = int(user_input.split()[0]), int(user_input.split()[1])

for x in range(decrease):
    if str(start)[-1] != '0': start -= 1
    else: start = int(str(start)[:-1])

print(start)