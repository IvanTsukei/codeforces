user_input = input()
count = {}
for word in list(user_input):
    try: count[word] += 1
    except KeyError: count[word] = 1

if len(count) % 2 == 0: print('CHAT WITH HER!')
else: print('IGNORE HIM!')