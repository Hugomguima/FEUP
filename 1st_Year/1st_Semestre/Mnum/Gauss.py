

matrix = [[7,2,0,24],
         [4,10,1,27],
         [5,-2,8,27]]

#print(matrix)

for i in range(3,-1,-1):
    matrix[0][i] /= matrix[0][0]
#print(matrix)

k10 = matrix[1][0]
for i in range(4):
    matrix[1][i] -= matrix[0][i]*k10
#print(matrix)
k20 = matrix[2][0]
for i in range(4):
    matrix[2][i] -= matrix[0][i]*k20
#print(matrix)
for i in range(3,-1,-1):
    matrix[1][i] /= matrix[1][1]
#print(matrix)
    
k21 = matrix[2][1]
for i in range(1,4):
    matrix[2][i] -= matrix[1][i]*k21

print(matrix)
    



    
    
    



































