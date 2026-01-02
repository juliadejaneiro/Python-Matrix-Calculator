# A simple real number matrix calculator using Python classes.
import numpy as np

class Matrix:
    def __intit___(self, m, n, array):
        self.rows = m
        self.cols = n
        self.matrix = array

class ZeroValueError(Exception):
    pass

def check_zero(m, n):
    if m == 0 or n == 0:
        raise ZeroValueError("value of 0 for matrix dimensions")
    return m, n
    

def main():
    try:
        get_dims = input('Enter the dimensions of the matrix separated by spaces: ')
        sep_dims = get_dims.split()

        # If a negative integer was passed, it will be changed to positive.
        # If the number is a float, it will be converted to int (rounded down).
        m = abs(int(sep_dims[0]))
        n = abs(int(sep_dims[1]))

        check_dims = check_zero(m, n)

    except ZeroValueError:
        print("Please enter nonzero values for the dimensions.")
        raise

    except ValueError:
        print("Input formatted incorrectly. Check for correct input types and space separation.")
        raise

    else:
        print("Program completed without errors.")
    
    print(f"Matrix dimensions: {check_dims[0]} x {check_dims[1]}")

    # Enter values for matrix entries. If the number of values is less than the number of entries, the remaining entries will be filled with 0's.

if __name__=="__main__":
    main()