user_input = int(input())

for x in range(0, user_input):
    length = input()
    all_items = input()
    all_items = [int(x) for x in all_items.split()]

    most_common = max(set(all_items), key=all_items.count)

    for x in range(len(all_items)):
        if all_items[x] != most_common: print(x+1)