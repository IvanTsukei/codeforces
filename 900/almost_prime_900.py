user_input = int(input())

def almost_prime(n):
    x, y, z = 2, 0, 1
    while n > 1:
        if n % x == 0:
            while n > 1:
                n /= x
                if n % x > 0: break
        if x == 3: z = 2
        x += z
        if n % x == 0:
            y += 1
            if y > 2: return False
    return y == 2

res = 0
    
for i in range(6, user_input + 1):
    if almost_prime(i):
        res += 1

print(res)