def maxIceCream(costs, coins):
    new_costs, spent, res = sorted(costs), 0, 0
    print(new_costs)

    if coins == 0 or min(costs) > coins: return 0
    for i in range(len(new_costs)):
        if spent == coins or (spent + new_costs[i]) > coins:
            return res
        if i == len(new_costs)-1:
            if spent == coins or (spent + new_costs[-1]) > coins:
                return res
        spent += new_costs[i]
        res += 1
    return res

print(maxIceCream([7,3,3,6,6,6,10,5,9,2], 56))