'''matrix = [['x','o','x'], ['x','o','x'], ['x','o','x']]
for x in matrix:
    for i in x:
        print(i)
    print
'''

x = 0
while x < len(matrix):
    i = 0
    while i < len(matrix[x]):
        print(matrix[x][i])
        i += 1
    x += 1
   
