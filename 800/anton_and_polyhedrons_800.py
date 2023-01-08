user_input = int(input())
check = {'Tetrahedron': 4, 'Cube': 6, 'Octahedron': 8, 'Dodecahedron': 12, 'Icosahedron': 20}
res = 0
for i in range(user_input): res += check.get(input())
print(res)