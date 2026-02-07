# Python Matrix Calculator
A simple matrix calculator to practice my Python and linear algebra skills.
This calculator performs basic operations (addition, subtraction, multiplication), although there are plans for additional functionalities.
The calculator assumes user input is correct; validation of user input is to be added.

## Known Issues
Temporarily remove matrix multiplication.
Errors with matrix multiplication on matrices of certain dimensions.

## Fixes
**2/07:** The Index Error caused by `transpose` method has been fixed.
The error stemmed from incorrect initialization of the matrix transpose with the `create_empty` method.
No parameters were passed, creating a matrix of the same dimensions as the input matrix.
This resulted in an Index Error for matrices where m != n, as the number of rows may exceed the number of columns or vice versa.


## Updates
**2/06:** Allow user to repeat operations without returning to the command menu.

## Operations
- Addition & subtraction (completed)
- Matrix multiplication (under revision as of 2/06)
- Transpose (completed)
- Inverse (incomplete)
- Conjugate transpose (incomplete)
- Unitary/not unitary (incomplete)

## Dependencies
This project requires the NumPy library. Use `pip install numpy` (pip) or `conda install numpy` (Anaconda) command(s).
For more information, consult the official NumPy resource: [NumPy - Installing NumPy](https://numpy.org/install/).

## Functionality
Run the Python script matrix_calculator.py.
You will encounter a menu of available commands. Enter the desired command when prompted.

<img width="180" height="173" alt="image" src="https://github.com/user-attachments/assets/3560517d-06e6-46c7-91b5-79ddbb4bf6d0" />




Specify the dimensions of the matrix by entering two int values with a space between.
Then, enter the appropriate number of entries with spaces between. The entries on each line represent a row in the matrix.

<img width="664" height="130" alt="image" src="https://github.com/user-attachments/assets/75c125a6-b4f7-4521-bdcd-710eddba9528" />



The result is displayed. The user may repeat the operation and enter values or return to the command menu.

<img width="229" height="184" alt="image" src="https://github.com/user-attachments/assets/f80b70cb-8e5a-426a-9df2-47166b760db0" />

