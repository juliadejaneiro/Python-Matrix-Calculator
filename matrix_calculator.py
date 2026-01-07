# A simple matrix calculator using Python classes.
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
    
    def create_empty(self):
        '''Create a new empty Matrix object of the same size as the Matrix object it is
        applied to.'''
        empty = np.zeros_like(self.matrix)
        empty_matrix = Matrix(self.m, self.n, empty)
        return empty_matrix
    
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

    def multiply(self, data_or_matrix):
        pass

    def inverse(self):
        pass

    def transpose(self):
        '''Create an empty matrix of the specified size.
        For each entry in the original matrix, switch the values in the index tuple.
        Place the entry in the new index of the empty matrix 
        (using change_entry) until all values are filled.'''
        new_row = []
        transposed = []
        for index, entry in np.ndenumerate(self.matrix):
            if index[1] == self.n:
                new_row.append(entry)
                transposed.append(new_row)
                new_row = []
            else:
                new_row.append(entry)
        return transposed

    def unitary(self):
        pass

def main():
    data = [[1, 2], [3, 4]]
    matrix1 = Matrix(2, 2, data)
    print(matrix1)

    print(matrix1.create_empty())

    # data2 = [[5, 6], [7, 8]]
    # matrix2 = Matrix(2, 2, data2)
    # print(matrix1)

    # result = matrix1.sub(matrix2)
    # print(result)

if __name__=="__main__":
    main()