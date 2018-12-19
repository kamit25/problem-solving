# Generate Magic Square of any matrix

# magic constant of a normal magic square is calculated on :
# constant = int(size * (((size * size)  + 1 )/2))
def generateMagicmagicsquare(n):
    # set zero as defult value to the matrix
    magicsquare = [[0 for x in range(n)] 
                 for y in range(n)] 
    # 1 is stored at position (n/2,n-1)
    i = int(n/2)
    j = n-1
    magicsquare[i][j] = 1 
    k = 2
    size = n**2
    # store remaining numbers in the matix
    while k < size+1:
        i -= 1
        j += 1
        # wrap the indices if index in out of bound
        if i == -1 and j == n:
            i = 0
            j = n - 2
        if i < 0:
            i = n - 1
        if j == n :
            j = 0
        #  to Check the position is occupied or not 
        if magicsquare[i][j] != 0:
            i += 1
            j -= 2
        # assign the number 
        magicsquare[i][j] = k
        k += 1
    
    for lst in range(len(magicsquare)):
        print(magicsquare[lst])
        
    
    
        
if __name__ == '__main__':
    matrix = 7    
    print('Magic Square of {} X {} matix'.format(matrix,matrix))
    generateMagicmagicsquare(matrix)
    