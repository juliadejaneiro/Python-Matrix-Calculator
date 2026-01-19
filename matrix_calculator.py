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
    
    def add(self, matrix_b):
        '''Add a Matrix object to another Matrix object.
        Both Matrix object and matrix_b must have the same dimensions.
        Takes one argument. 
        matrix_b: Matrix object'''
        # result = self.matrix + matrix_b.matrix
        added =  self.create_empty(self.m, self.n)
        for index, entry in np.ndenumerate(self.matrix):
            added_entry = entry + matrix_b.matrix[index[0], index[1]]
            added.matrix[index[0], index[1]] += added_entry
        return added
    
    def sub(self, matrix_b):
        '''Subtract a Matrix object from another Matrix object, ndarray, or nested list.
        Both Matrix object and data_or_matrix must have the same dimensions.
        Takes one argument.
        matrix_b: Matrix object'''
        subtracted =  self.create_empty(self.m, self.n)
        for index, entry in np.ndenumerate(self.matrix):
            subtracted_entry = entry - matrix_b.matrix[index[0], index[1]]
            subtracted.matrix[index[0], index[1]] += subtracted_entry
        return subtracted

    def multiply(self, matrix_b):
        '''Multiply the Matrix object (A) with another Matrix object, ndarray, or nested list (B).
        Number of columns in A must match number of rows in B.
        Calculates AB = C.
        Takes one argument.
        matrix_b: Matrix object, ndarray, or nested list'''
        # Create empty matrix with dimensions n (columns of A) and p (rows of B).
        multiplied =  self.create_empty(self.n, len(matrix_b.matrix))
        for index, entry in np.ndenumerate(self.matrix):
            multiply_values = matrix_b.matrix[index[1]]
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
    
    while True:
        print('\nAVAILABLE COMMANDS')
        print('--------------------')
        print('Add',
        'Subtract',
        'Multiply',
        'Transpose',
        'X to quit', sep='\n')

        response = input('\nEnter a command.\n').lower()

        match response:
            case 'x':
                print('Goodbye!')
                break

            case 'add' | 'sub' | 'subtract':
                dims_str = input('\nEnter number of rows and columns separated by a space: ')
                dims_list = list(map(int, dims_str.split()))
                rows, cols = dims_list[0], dims_list[1]

                print(f'Enter the {cols} entries for each row of the first matrix (A): ')
                data_a = [list(map(int, input().split())) for _ in range(rows)]
                matrix_a = Matrix(rows, cols, data_a)

                print(f'Enter the {cols} entries for each row of the second matrix (B): ')
                data_b = [list(map(int, input().split())) for _ in range(rows)]
                matrix_b = Matrix(rows, cols, data_b)
                
                if response == 'add':
                    print('\nResult of adding:\n', matrix_a.add(matrix_b))
                else:
                    print('\nResult of subtracting:\n', matrix_a.sub(matrix_b))

            case 'multiply':
                dims_a_str = input('\nEnter number of rows and columns for matrix A (separated by a space): ')
                dims_a_list = list(map(int, dims_a_str.split()))
                rows_a, cols_a = dims_a_list[0], dims_a_list[1]

                print(f'Enter the {cols_a} entries for each row of matrix A (separated by space): ')
                data_a = [list(map(int, input().split())) for _ in range(rows_a)]
                matrix_a = Matrix(rows_a, cols_a, data_a)

                cols_b_str = input('\nEnter number of columns for matrix B: ')
                cols_b = int(cols_b_str)

                print(f'Enter the {cols_b} entries for each row of matrix B (separated by space): ')
                data_b = [list(map(int, input().split())) for _ in range(cols_a)]
                matrix_b = Matrix(cols_a, cols_b, data_b)

                print('\n Result of multiplication:\n', matrix_a.multiply(matrix_b))

            case 'transpose':
                dims_str = input('\nEnter number of rows and columns separated by a space: ')
                dims_list = list(map(int, dims_str.split()))
                rows, cols = dims_list[0], dims_list[1]

                print(f'Enter the {cols} entries for each row of the matrix to transpose (separated by space): ')
                data_a = [list(map(int, input().split())) for _ in range(rows)]
                matrix_a = Matrix(rows, cols, data_a)
                print('\nResult of transpose:\n', matrix_a.transpose())

            case _:
                print('Unknown command. Please enter a valid command from the menu.')

if __name__=="__main__":
    main()