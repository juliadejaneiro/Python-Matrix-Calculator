# A simple real number matrix calculator using Python classes.
import numpy as np

class Matrix:
    def __init__(self, m, n, data):
        '''Set Matrix object attributes.
        m : number of columns
        n: number of rows
        data: nested list or nparray'''
        self.m = m
        self.n = n
        self.matrix = np.array(data)

    def __str__(self):
        '''Print Matrix object with dimensions.'''
        print_str = "{}\n with dimensions {} x {}".format(self.matrix, self.m, self.n)
        return print_str
    
    def change_entry(self, m, n, new_value):
        '''Change an entry in the Matrix.
        Three arguments.
        m: column
        n: row
        new_value: a value to replace entry in row m column n'''
        self.matrix[m, n] = new_value
        print(self)
        return self.matrix
    
    def add(self, data_or_matrix):
        '''Add a Matrix object to another Matrix object, nparray, or nested list.
        Both Matrix object and data_or_matrix must have the same dimensions.
        Takes one argument: 
        data_or_matrix: Matrix object, nparray, or nested list. '''
        if isinstance(data_or_matrix, Matrix):
            result = self.matrix + data_or_matrix.matrix
        else:
            add_matrix = np.array(data_or_matrix)
            result = np.add(self.matrix, add_matrix)
        return result
    
    def sub(self, data_or_matrix):
        '''Subtract a Matrix object from another Matrix object, nparray, or nested list.
        Both Matrix object and data_or_matrix must have the same dimensions.
        Takes one argument.
        data_or_matrix: Matrix object, nparray, or nested list. '''
        if isinstance(data_or_matrix, Matrix):
            result = self.matrix - data_or_matrix.matrix
        else:
            add_matrix = np.array(data_or_matrix)
            result = np.subtract(self.matrix, add_matrix)
        return result

data = [[1, 2], [3, 4]]
matrix1 = Matrix(2, 2, data)
print(matrix1)

matrix1.change_entry(0, 0, 4)

# data2 = [[5, 6], [7, 8]]
# matrix2 = Matrix(2, 2, data2)
# print(matrix1)

# result = matrix1.sub(matrix2)
# print(result)

# def main():
#     try:
#         get_dims = input('Enter the dimensions of the matrix separated by spaces: ')
#         sep_dims = get_dims.split()

#         # If a negative integer was passed, it will be changed to positive.
#         # If the number is a float, it will be converted to int (rounded down).
#         m = abs(int(sep_dims[0]))
#         n = abs(int(sep_dims[1]))

#         check_dims = check_zero(m, n)

#     except ZeroValueError:
#         print("Please enter nonzero values for the dimensions.")
#         raise

#     except ValueError:
#         print("Input formatted incorrectly. Check for correct input types and space separation.")
#         raise

#     else:
#         print("Program completed without errors.")
    
#     print(f"Matrix dimensions: {check_dims[0]} x {check_dims[1]}")

#     # Enter values for matrix entries. If the number of values is less than the number of entries, the remaining entries will be filled with 0's.

# if __name__=="__main__":
#     main()