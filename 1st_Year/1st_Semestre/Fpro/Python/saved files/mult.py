
def mult(M,N):
   rows_M = len(M)
   cols_M = len(M[0])
   rows_N = len(N)
   cols_N = len(N[0])
   result = []
   new_N = []
   
   
   if cols_M != rows_N:
       return result
   
#   for i in range(cols_N):
#       new_row = []
#       for j in range(rows_N):
#           new_row += [N[j][i]]
#           new_N.append(new_row)
#   
#   rows_new_N = len(new_N)
#   cols_new_N = len(new_N[0])
           
    
   for i in range(rows_M):
       for j in range(cols_N):
           for k in range(cols_M):
               product = M[i][k] * N[i][j]
               print(product)
           
    
   return result
    