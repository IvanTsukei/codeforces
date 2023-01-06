user_input = int(input())

for x in range(0, user_input):
    lucky_number = input()
    all_items = [int(x) for x in str(lucky_number)]
    if sum(all_items[:3]) == sum(all_items[3:]): print('YES')
    else: print('NO')