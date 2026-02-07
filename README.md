# Python Matrix Calculator
A simple matrix calculator to practice my Python and linear algebra skills.
This calculator performs basic operations (addition, subtraction, multiplication), although there are plans for additional functionalities.
The calculator assumes user input is correct; validation of user input is to be added.

## Known Issues
Temporarily remove matrix multiplication.
Errors with matrix multiplication on matrices of certain dimensions.

## Fixes
(6/07)
The Index Error encountered with transpose operation has been fixed.
The error stemmed from incorrect initialization of the transposed matrix with the `create_empty` method.
No parameters were passed, creating a matrix of the same dimensions as the input matrix.
This resulted in an Index Error for matrices where m != n, as the number of columns may exceed the number of rows or vice versa.


## Updates
Allow user to repeat operations without returning to the command menu.

## Operations
- Addition & subtraction (completed)
- Matrix multiplication (under revision)
- Transpose (under revision)
- Inverse (incomplete)
- Conjugate transpose (incomplete)
- Unitary/not unitary (incomplete)

## Dependencies
This project requires the NumPy library. Use `pip install numpy` (pip) or `conda install numpy` (Anaconda) command(s).
For more information, consult the official NumPy resource: [NumPy - Installing NumPy](https://numpy.org/install/).

## Functionality
Run the Python script matrix_calculator.py.
You will encounter a menu of available commands. Enter the desired command when prompted.

<img width="170" height="219" alt="image" src="https://github.com/user-attachments/assets/3d60480e-6967-4860-80f0-6715947a2b76" />



Specify the dimensions of the matrix by entering two int values with a space between.
Then, enter the appropriate number of entries with spaces between. The entries on each line represent a row in the matrix.

<img width="596" height="188" alt="example" src="https://github.com/user-attachments/assets/6cdb98fa-bfd1-4ed4-8d0f-1267d4f573b3" />


The result is displayed, and the menu commands will once again reappear.

<img width="237" height="382" alt="results" src="https://github.com/user-attachments/assets/e41ccf09-ff93-4b37-bfec-fe48703c5fef" />
