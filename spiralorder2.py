'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Given n = 3,

You should return the following matrix:

[
  [ 1, 2, 3 ],
  [ 8, 9, 4 ],
  [ 7, 6, 5 ]
]
'''
def generateMatrix(self, n):
    A, lo = [], n*n+1
    while lo > 1:
        lo, hi = lo - len(A), lo
        A = [range(lo, hi)] + zip(*A[::-1])
    return A
#SOLUTION 2
''' 
(1) Create a matrix to store the coordinates

(0,0) (0,1) (0,2)

(1,0) (1,1) (1,2)

(2,0) (2,1) (2,2)

(2) Read it out using the trick of "Spiral Matrix I"

(0,0) (0,1) (0,2) (1,2) (2,2) ...

(3) Put 1, 2, 3, ... n**2 at these coordinates sequentially. Done.
'''

def generateMatrix(n):
    
    result = [[0 for i in range(n)] for j in range(n)]
    coord = [[(i,j) for j in range(n)] for i in range(n)]
    
    count = 1
    
    while coord:
        for x, y in coord.pop(0):
            result[x][y] = count
            count += 1
            print(result)
        coord = zip(*coord)[::-1]

    return result
  
  
