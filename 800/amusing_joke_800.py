guest_1, host_1, combo = input(), input(), input()
check = {x:list(guest_1+host_1).count(x) for x in list(guest_1+host_1)}
combo_dict = {x:combo.count(x) for x in list(combo)}

if check == combo_dict: print('YES')
else: print('NO')