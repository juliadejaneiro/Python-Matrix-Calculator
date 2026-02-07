# A simple matrix calculator using Python classes.
import numpy as np

class Matrix:
    """A Matrix object to perform matrix operations.

    Attributes:
        m : int indicating the number of columns.
        n: int indicating the number of rows.
        data: nested list of numerical matrix entries.
    """

    def __init__(self, m, n, data):
        """Initialize Matrix object.

        Arguments:
            m: set the number of columns.
            n: set the number of rows.
            data: content of the matrix.
        """
        self.m = m
        self.n = n
        self.matrix = np.array(data)

    def __str__(self):
        """Print Matrix object with dimensions."""
        print_str = "{}\n with dimensions {} x {}".format(self.matrix, self.m, self.n)
        return print_str
    
    def create_empty(self, *args):
        """Create a new empty Matrix object of the same dimensions as the Matrix object it is
        called on.

        Arguments:
            *args: int value(s) to create a Matrix of a specified size

        If only one additional argument, the value is used for both dimensions (m x m).
        If more than two values in args, only the first two are considered (m x n).
        """
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
        """Change an entry in the Matrix.

        Arguments:
            m: int row number.
            n: int column number.
            new_value: a numerical value to replace entry in row m column n.
        """
        self.matrix[m, n] = new_value
        return self.matrix
    
    def add(self, matrix_b):
        """Add a Matrix object to another Matrix object.
        Both Matrix object and matrix_b must have the same dimensions.

        Arguments:
            matrix_b: Matrix object.
        """
        added =  self.create_empty(self.m, self.n)
        for index, entry in np.ndenumerate(self.matrix):
            added_entry = entry + matrix_b.matrix[index[0], index[1]]
            added.matrix[index[0], index[1]] += added_entry
        return added
    
    def sub(self, matrix_b):
        """Subtract a Matrix object from another Matrix object.
        Both Matrix object and matrix_b must have the same dimensions.

        Arguments:
            matrix_b: Matrix object.
        """
        subtracted =  self.create_empty(self.m, self.n)
        for index, entry in np.ndenumerate(self.matrix):
            subtracted_entry = entry - matrix_b.matrix[index[0], index[1]]
            subtracted.matrix[index[0], index[1]] += subtracted_entry
        return subtracted

    def multiply(self, matrix_b):
        """Multiply the Matrix object (A) with another Matrix object (B).
        Number of columns in A must match number of rows in B.

        Arguments:
            matrix_b: Matrix object.
        """
        columns_b = matrix_b.matrix.shape[1]
        # Create empty matrix with dimensions m (rows of A) and p (columns of B).
        multiplied =  self.create_empty(self.m, columns_b)
        # For each entry in matrix A, take the values from matrix B to multiply with.
        for a_index, entry in np.ndenumerate(self.matrix):
            # The values from B correspond to the column number of the matrix A entry.
            b_values = matrix_b.matrix[a_index[1]]
            # Multiply entry from A with each value from B to produce a new_value.
            for b_index, b_value in enumerate(b_values):
                new_value = entry * b_value
                # Add each new_value to the correct position in the multiplied matrix.
                # The correct position is the row of entry A and the column of each
                # value in b_values.
                multiplied.matrix[a_index[0], b_index] += new_value
        return multiplied

    def inverse(self):
        pass

    def transpose(self):
        """For each entry in the original matrix, switch the values in the index tuple. (index[1], index[0])
        Place the entry in the empty matrix (using change_entry) until all values are filled.
        """
        transposed = self.create_empty(self.n, self.m)
        for index, entry in np.ndenumerate(self.matrix):
            print(index)
            transposed.matrix[index[1], index[0]] += entry
        return transposed

    def unitary(self):
        pass

    def conjugate_transpose(self):
        pass

def main():
    
    while True:
        print('\nAVAILABLE COMMANDS')
        print('--------------------')
        print('Add',
        'Subtract',
        'Transpose',
        'X to quit', sep='\n')

        response = input('\nEnter a command.\n').lower()

        match response:
            case 'x':
                print('Goodbye!')
                break

            case 'add' | 'sub' | 'subtract':
                repeat = ""
                while repeat != 'n':
                    dims_str = input('\nEnter number of rows and columns separated by a space: ')
                    dims_list = list(map(int, dims_str.split()))
                    rows, cols = dims_list[0], dims_list[1]

                    print(f'Enter the {cols} entries for each row of the first matrix (separated by a space): ')
                    data_a = [list(map(int, input().split())) for _ in range(rows)]
                    matrix_a = Matrix(rows, cols, data_a)

                    print(f'Enter the {cols} entries for each row of the second matrix (separated by a space): ')
                    data_b = [list(map(int, input().split())) for _ in range(rows)]
                    matrix_b = Matrix(rows, cols, data_b)
                
                    if response == 'add':
                        print('\nResult of adding:\n', matrix_a.add(matrix_b))
                        repeat = input('\nDo another addition? (y/n)\n').lower()
                    else:
                        print('\nResult of subtracting:\n', matrix_a.sub(matrix_b))
                        repeat = input('\nDo another subtraction? (y/n)\n').lower()

                    match repeat:
                        case 'n':
                            print('\nReturning to menu.')
                        case repeat if repeat != 'y':
                            print('\nInvalid input. Terminating operation.')
                            break

            # case 'multiply':
            #     repeat = ""
            #     while repeat != 'n':
            #         dims_a_str = input('\nEnter number of rows and columns for the first matrix: ')
            #         dims_a_list = list(map(int, dims_a_str.split()))
            #         rows_a, cols_a = dims_a_list[0], dims_a_list[1]

            #         print(f'Enter the {cols_a} entries for each row of the first matrix (separated by a space): ')
            #         data_a = [list(map(int, input().split())) for _ in range(rows_a)]
            #         matrix_a = Matrix(rows_a, cols_a, data_a)

            #         cols_b_str = input('\nEnter number of columns for the second matrix: ')
            #         cols_b = int(cols_b_str)

            #         print(f'Enter the {cols_b} entries for each row of the second matrix (separated by a space): ')
            #         data_b = [list(map(int, input().split())) for _ in range(cols_a)]
            #         matrix_b = Matrix(cols_a, cols_b, data_b)
            #         print('\nResult of multiplication:\n', matrix_a.multiply(matrix_b))
                    
            #         repeat = input('\nDo another multiplication? (y/n)\n').lower()
            #         match repeat:
            #             case 'n':
            #                 print('\nReturning to menu.')
            #             case repeat if repeat != 'y':
            #                 print('\nInvalid input. Terminating operation.')
            #                 break

            case 'transpose':
                repeat = ""
                while repeat != 'n':
                    dims_str = input('\nEnter number of rows and columns separated by a space: ')
                    dims_list = list(map(int, dims_str.split()))
                    rows, cols = dims_list[0], dims_list[1]

                    print(f'Enter the {cols} entries for each row of the matrix to transpose (separated by space): ')
                    data_a = [list(map(int, input().split())) for _ in range(rows)]
                    matrix_a = Matrix(rows, cols, data_a)
                    print('\nResult of transpose:\n', matrix_a.transpose())

                    repeat = input('\nDo another transpose? (y/n)\n').lower()
                    match repeat:
                        case 'n':
                             print('\nReturning to menu.')
                        case repeat if repeat != 'y':
                            print('\nInvalid input. Terminating operation.')
                            break

            case _:
                print('Unknown command. Please enter a valid command from the menu.')

if __name__=="__main__":
    main()