def matrix(mat,n):
    row_sum=0
    col_sum=0
    for i in range(n):
        row_sum+=mat[n//2][i]
    print(row_sum)    
    for j in range(n):
        col_sum+=mat[j][n//2]
    print(col_sum)    
mat=[[1,4,5],
     [5,7,8],
     [8,6,5]]
matrix(mat,3)
