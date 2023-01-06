user_input = int(input())

for _ in range(0, user_input):
    n = input()
    if len(n) <= 10:
        print(n)
    else:
        temp = len(n)-2
        print(f'{n[0]}{temp}{n[-1]}')