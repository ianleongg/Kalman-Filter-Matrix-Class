import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h ==1:
            det = self.g[0][0]
        else:
            a = self.g [0][0]
            b = self.g [0][1]
            c = self.g [1][0]
            d = self.g [1][1]
            
            det = a * d - b * c
        return det
    
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        tra = 0
        for i in range(self.h):
            tra += self.g[i][i]
        return tra

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        inverse = []
        if len(self.g) == 1:
            inverse.append([1/ self [0][0]])
        elif len (self.g) == 2:
            a = self [0][0]
            b = self [0][1]
            c = self [1][0]
            d = self [1][1]
            
            factor = 1 / (a * d - b * c)
            
            inverse = [[d, -b],[-c, a]]
            
            for i in range(len(inverse)):
                for j in range(len(inverse[0])):
                    inverse[i][j] = factor * inverse[i][j]
    
        return Matrix(inverse)
            

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
    # Loop through columns on outside loop
        for j in range(len(self.g[0])):
            new_row = []
            # Loop through columns on inner loop
            for i in range(len(self.g)):
                # Column values will be filled by what were each row before
                new_row.append(self[i][j])
            matrix_transpose.append(new_row)

        return Matrix(matrix_transpose)

    def is_square(self):
            return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        
        matrixSum = []
    
        # matrix to hold a row for appending sums of each element
        row = []
    
        # For loop within a for loop to iterate over the matrices
        for i in range(len(self.g)):
            row = [] # reset the list
            for j in range(len(self.g[0])):
                row.append(self.g[i][j] + other.g[i][j]) # add the matrices
            matrixSum.append(row)

        return Matrix(matrixSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        result = []
        for i in range(len(self.g)):
            temp = []
            for j in range(len(self.g[0])):
                temp.append(-self.g[i][j])
            result.append(temp)
        
        return Matrix(result)
    
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        result = []
        
        for i in range(len(self.g)):
            temp=[]
            for j in range(len(self.g[0])):
                temp.append(self.g[i][j]-other.g[i][j])
            result.append(temp)
        return Matrix(result)
    

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
       
        result = []
        
        other_T = []
        for i in range(other.w):
            temp = []
            for j in range(other.h):
                temp.append(other[j][i])
            other_T.append(temp)
            
        for i in range(len(self.g)):
            temp = []
            for j in range(len(other_T)):
                val = 0
                for k in range(len(self.g[0])):
                    val = val + self.g[i][k] * other_T[j][k]
                temp.append(val)
            result.append(temp)
        
        return Matrix(result)
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
    
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            result = []
            for i in range(len(self.g)):
                temp = []
                for j in range(len(self.g[0])):
                    temp.append(other* self [i][j])
                result.append(temp)
            return Matrix(result)
            