Sparse Matrix Operations - README
Project Overview
This Python program implements sparse matrix operations (addition, subtraction, multiplication) using an efficient storage format.

#Features
✔ Reads sparse matrices from files
✔ Supports addition, subtraction, and multiplication
✔ Handles large matrices efficiently
✔ Validates input file format
✔ Allows saving results to a file

#Setup & Execution

#File Structure

/dsa/sparse_matrix/  
├── code/  
│   └── src/  
│       └── sparse_matrix.py  # Main program  
└── sample_inputs/  
    ├── matrix1.txt          # Example input  
    └── matrix2.txt          # Example input  
#How to Run

Navigate to the src folder:

cd /dsa/sparse_matrix/code/src/

Run the program:

python3 sparse_matrix.py

Follow the menu prompts to perform operations.

#Input File Format
Each matrix file must follow this structure:

rows=3  
cols=3  
(0, 0, 1)  
(1, 1, 2)  
(2, 2, 3)  
First two lines define rows and columns.
Subsequent lines list non-zero values in (row, col, value) format.
#Supported Operations

Addition (A + B)
Matrices must have the same dimensions.
Subtraction (A - B)
Matrices must have the same dimensions.
Multiplication (A × B)
Columns of A must match rows of B.
#Example Usage

Load two matrices (matrix1.txt and matrix2.txt).
Select an operation (1: Add, 2: Subtract, 3: Multiply).
View the result or save to a file.
Error Handling
❌ Invalid matrix dimensions
❌ Incorrect file format
❌ Out-of-bound indices
#Quick Start

git clone
cd dsa/sparse_matrix/code/src
python3 sparse-matrix.py