a, b = str(input()), str(input())
c = int(a, 2)^int(b,2)
print(bin(c)[2:].zfill(len(a)))
