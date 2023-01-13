user_input = int(input())
res, current = 0, user_input
nums = [5, 4, 3, 2, 1]
for i in nums:
    if divmod(current, i)[0] != 0: 
        res += divmod(current, i)[0]
        current = current - divmod(current, i)[0]*i

print(res)