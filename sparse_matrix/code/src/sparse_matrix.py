"""
Sparse Matrix Operations

Author: [Your Name]
Description: This program reads two sparse matrices from input files,
             performs addition, subtraction, or multiplication, and writes
             the result to an output file. The matrices are stored using
             custom data structures to optimize memory usage.

Note: No built-in libraries (like numpy or regex) are used as per assignment rules.
"""

class SparseMatrix:
    def __init__(self, file_path=None, rows=None, cols=None):
        """
        Initialize a sparse matrix either from file or using dimensions.
        """
        self.data = {}  # Dictionary to store non-zero values with keys as (row, col)
        if file_path:
            self._load_from_file(file_path)
        else:
            self.rows = rows
            self.cols = cols

    def _load_from_file(self, file_path):
        """
        Reads matrix from a file in sparse format.
        File format:
            rows=3
            cols=3
            (0, 1, 5)
            (1, 2, 8)
        """
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Read rows and columns
            self.rows = int(lines[0].split('=')[1].strip())
            self.cols = int(lines[1].split('=')[1].strip())

            for line in lines[2:]:
                line = line.strip().replace(' ', '')
                if not line:
                    continue  # Skip empty lines

                # Validate line format
                if not (line.startswith('(') and line.endswith(')')):
                    raise ValueError("Input file has wrong format")

                line = line[1:-1]  # Remove surrounding parentheses
                parts = line.split(',')

                if len(parts) != 3:
                    raise ValueError("Input file has wrong format")

                row, col, value = parts

                if '.' in row or '.' in col or '.' in value:
                    raise ValueError("Floating point values are not allowed")

                self.setElement(int(row), int(col), int(value))

        except Exception:
            raise ValueError("Input file has wrong format")

    def getElement(self, row, col):
        """
        Get the value at a specific position. Returns 0 if not present.
        """
        return self.data.get((row, col), 0)

    def setElement(self, row, col, value):
        """
        Set a value at a specific position. If value is 0, removes the entry.
        """
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def add(self, other):
        """
        Add two sparse matrices.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix size mismatch for addition")

        result = SparseMatrix(rows=self.rows, cols=self.cols)
        keys = set(self.data.keys()).union(other.data.keys())

        for key in keys:
            val = self.getElement(*key) + other.getElement(*key)
            result.setElement(*key, val)

        return result

    def subtract(self, other):
        """
        Subtract another sparse matrix from this matrix.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix size mismatch for subtraction")

        result = SparseMatrix(rows=self.rows, cols=self.cols)
        keys = set(self.data.keys()).union(other.data.keys())

        for key in keys:
            val = self.getElement(*key) - other.getElement(*key)
            result.setElement(*key, val)

        return result

    def multiply(self, other):
        """
        Multiply two sparse matrices.
        """
        if self.cols != other.rows:
            raise ValueError("Matrix size mismatch for multiplication")

        result = SparseMatrix(rows=self.rows, cols=other.cols)

        # Matrix multiplication logic
        for (i, k1), v1 in self.data.items():
            for j in range(other.cols):
                v2 = other.getElement(k1, j)
                if v2 != 0:
                    existing = result.getElement(i, j)
                    result.setElement(i, j, existing + v1 * v2)

        return result

    def save_to_file(self, filename):
        """
        Save matrix to file in the same sparse format.
        """
        with open(filename, 'w') as f:
            f.write(f"rows={self.rows}\n")
            f.write(f"cols={self.cols}\n")
            for (row, col), val in sorted(self.data.items()):
                f.write(f"({row}, {col}, {val})\n")


# ---------------------------
# CLI Interface for User
# ---------------------------

def main():
    """
    Command-Line Interface: Allows user to choose operation and input files.
    """
    print("Sparse Matrix Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")

    choice = input("Enter 1, 2, or 3: ").strip()
    path1 = input("Enter path to first matrix file: ").strip()
    path2 = input("Enter path to second matrix file: ").strip()

    try:
        # Load matrices
        A = SparseMatrix(file_path=path1)
        B = SparseMatrix(file_path=path2)

        if choice == '1':
            result = A.add(B)
            result.save_to_file("result_add.txt")
            print("Addition completed. Result saved to result_add.txt.")
        elif choice == '2':
            result = A.subtract(B)
            result.save_to_file("result_subtract.txt")
            print("Subtraction completed. Result saved to result_subtract.txt.")
        elif choice == '3':
            result = A.multiply(B)
            result.save_to_file("result_multiply.txt")
            print("Multiplication completed. Result saved to result_multiply.txt.")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    except ValueError as ve:
        print(f"Error: {ve}")

# Entry point for script
if __name__ == "__main__":
    main()
