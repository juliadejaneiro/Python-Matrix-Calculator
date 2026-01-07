# A simple matrix calculator using Python classes.
import numpy as np

class Matrix:
    def __init__(self, m, n, data):
        '''Set Matrix object attributes.
        m : number of columns
        n: number of rows
        data: nested list or ndarray'''
        self.m = m
        self.n = n
        self.matrix = np.array(data)

    def __str__(self):
        '''Print Matrix object with dimensions.'''
        print_str = "{}\n with dimensions {} x {}".format(self.matrix, self.m, self.n)
        return print_str
    
    def create_empty(self, *args):
        '''Create a new empty Matrix object of the same dimensions as the Matrix object it is
        applied to.
        *args: int value(s) to create a Matrix of a specified size
        If only one additional argument, the value is used for both dimensions (m x m).
        If more than two values in args, only the first two are considered (m x n).'''
        if args and len(args) >= 2:
            empty_matrix = Matrix(args[0], args[1],  np.zeros_like(self.matrix, shape=(args[0], args[1])))
        elif args and len(args) == 1:
            empty_matrix = Matrix(args[0], args[0],  np.zeros_like(self.matrix, shape=(args[0], args[0])))
        else:
            empty_matrix = Matrix(self.m, self.n, np.zeros_like(self.matrix))
        return empty_matrix
    
    def get_entry(self, m, n):
        return self.matrix[m, n]
    
    def change_entry(self, m, n, new_value):
        '''Change an entry in the Matrix.
        Three arguments.
        m: column
        n: row
        new_value: a value to replace entry in row m column n'''
        self.matrix[m, n] = new_value
        return self.matrix
    
    def add(self, data_or_matrix):
        '''Add a Matrix object to another Matrix object, nparray, or nested list.
        Both Matrix object and data_or_matrix must have the same dimensions.
        Takes one argument. 
        data_or_matrix: Matrix object, nparray, or nested list. '''
        if isinstance(data_or_matrix, Matrix):
            result = self.matrix + data_or_matrix.matrix
        else:
            add_matrix = np.array(data_or_matrix)
            result = np.add(self.matrix, add_matrix)
        return result
    
    def sub(self, data_or_matrix):
        '''Subtract a Matrix object from another Matrix object, ndarray, or nested list.
        Both Matrix object and data_or_matrix must have the same dimensions.
        Takes one argument.
        data_or_matrix: Matrix object, nparray, or nested list'''
        if isinstance(data_or_matrix, Matrix):
            result = self.matrix - data_or_matrix.matrix
        else:
            add_matrix = np.array(data_or_matrix)
            result = np.subtract(self.matrix, add_matrix)
        return result

    def multiply(self, data_or_matrix):
        '''Multiply the Matrix object (A) with another Matrix object, ndarray, or nested list (B).
        Number of columns in A must match number of rows in B.
        Calculates AB = C.
        Takes one argument.
        data_or_matrix: Matrix object, ndarray, or nested list'''
        multiplied = self.create_empty(self.n, len(data_or_matrix))
        for index, entry in np.ndenumerate(self.matrix):
            multiply_values = data_or_matrix[index[1]]
            # print("The value is:", entry)
            # print("The multipliers are", multiply_values)
            for vindex, value in enumerate(multiply_values):
                new_value = entry * value
                multiplied.matrix[index[0], vindex] += new_value
        return multiplied

    def inverse(self):
        pass

    def transpose(self):
        '''Create an empty matrix of the specified size.
        For each entry in the original matrix, switch the values in the index tuple. (index[1], index[0])
        Place the entry in the new index of the empty matrix 
        (using change_entry) until all values are filled.'''
        transposed = self.create_empty()
        for index, entry in np.ndenumerate(self.matrix):
                transposed.change_entry(index[1], index[0], entry)
        return transposed

    def unitary(self):
        pass

def main():
    data = [[1, 2], [3, 4]]
    matrix1 = Matrix(2, 2, data)
    print(matrix1)
    print(matrix1.create_empty(3, 4, 5))
    # print(matrix1.transpose())

    data2 = [[5, 6], [7, 8]]
    matrix2 = Matrix(2, 2, data2)
    # print(matrix1)
    print(matrix1.multiply(matrix2))
    # result = matrix1.sub(matrix2)
    # print(result)

if __name__=="__main__":
    main()