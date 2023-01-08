houses = str(input())
list_homes = sorted([int(i) for i in houses.split()])
print(sum([(list_homes[2]-list_homes[1]), (list_homes[1]-list_homes[0])]))
