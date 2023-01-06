user_input = int(input())

for x in range(0, user_input):
    sum_test = input()
    all_items = [int(x) for x in sum_test.split()]
    max_num = max(all_items)
    all_items.remove(max_num)
    if sum(all_items) == max_num: print('YES')
    else: print('NO')