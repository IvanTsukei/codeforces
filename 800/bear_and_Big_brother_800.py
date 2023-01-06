user_input = input()
user_input = user_input.split()
limak, bob = int(user_input[0]), int(user_input[1])

res = 0
while limak <= bob:
    limak = limak * 3
    bob = bob * 2
    res += 1

print(res)