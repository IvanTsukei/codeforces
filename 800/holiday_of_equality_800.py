citizens, welfare = int(input()), str(input())
list_welfare, res = [int(i) for i in welfare.split()], 0

for i in list_welfare: 
    if i < max(list_welfare): res += (max(list_welfare) - i)

print(res)
