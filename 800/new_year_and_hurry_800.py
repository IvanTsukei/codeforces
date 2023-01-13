user_input = input()
time_vars = user_input.split()
contest_time, solved, time_used =  240 - int(time_vars[1]), 0, 0

for i in range(1, int(time_vars[0])+1):
    if time_used + (5*i) > contest_time: break
    elif contest_time <= 0: 
        print(0)
    else: 
        time_used += 5*i
        solved += 1
print(solved)