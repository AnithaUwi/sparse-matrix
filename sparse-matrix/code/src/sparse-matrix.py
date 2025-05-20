class SparseMatrix:
    def __init__(self, numRows=None, numCols=None, filePath=None):
        self.rows = numRows
        self.cols = numCols
        self.matrix = {}  # (row, col) -> value
        
        if filePath:
            self.load_from_file(filePath)
    
    def load_from_file(self, filePath):
        """Load matrix from file"""
        try:
            with open(filePath, 'r') as file:
                lines = [line.strip() for line in file if line.strip()]
                
                # Parse rows and cols
                if not lines[0].startswith('rows=') or not lines[1].startswith('cols='):
                    raise ValueError("Input file has wrong format")
                
                self.rows = int(lines[0][5:])
                self.cols = int(lines[1][5:])
                
                # Parse entries
                for line in lines[2:]:
                    if not (line.startswith('(') and line.endswith(')')):
                        raise ValueError("Input file has wrong format")
                    
                    content = line[1:-1].split(',')
                    if len(content) != 3:
                        raise ValueError("Input file has wrong format")
                    
                    row = int(content[0].strip())
                    col = int(content[1].strip())
                    value = int(content[2].strip())
                    
                    self.setElement(row, col, value)
                    
        except (ValueError, IndexError) as e:
            raise ValueError("Input file has wrong format") from e
    
    def getElement(self, currRow, currCol):
        """Get value at (row, col)"""
        if currRow >= self.rows or currCol >= self.cols or currRow < 0 or currCol < 0:
            raise IndexError("Index out of bounds")
        return self.matrix.get((currRow, currCol), 0)
    
    def setElement(self, currRow, currCol, value):
        """Set value at (row, col)"""
        if currRow >= self.rows or currCol >= self.cols or currRow < 0 or currCol < 0:
            raise IndexError("Index out of bounds")
        if value != 0:
            self.matrix[(currRow, currCol)] = value
        elif (currRow, currCol) in self.matrix:
            del self.matrix[(currRow, currCol)]
    
    def add(self, other):
        """Add two matrices"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition")
        result = SparseMatrix(self.rows, self.cols)
        # (Rest of the add function from earlier)
    
    def subtract(self, other):
        """Subtract two matrices"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for subtraction")
        result = SparseMatrix(self.rows, self.cols)
        # (Rest of the subtract function from earlier)
    
    def multiply(self, other):
        """Multiply two matrices"""
        if self.cols != other.rows:
            raise ValueError("Number of columns in first matrix must match rows in second")
        result = SparseMatrix(self.rows, other.cols)
        # (Rest of the multiply function from earlier)
    
    def __str__(self):
        """String representation of matrix"""
        result = []
        for row in range(self.rows):
            row_data = []
            for col in range(self.cols):
                row_data.append(str(self.getElement(row, col)))
            result.append(' '.join(row_data))
        return '\n'.join(result)

def main():
    print("Sparse Matrix Operations")
    print("1. Add two matrices")
    print("2. Subtract two matrices")
    print("3. Multiply two matrices")
    print("4. Exit")
    
    while True:
        choice = input("Enter your choice (1-4): ")
        
        if choice == '4':
            break
        
        try:
            file1 = input("Enter path to first matrix file: ")
            file2 = input("Enter path to second matrix file: ")
            
            matrix1 = SparseMatrix(filePath=file1)
            matrix2 = SparseMatrix(filePath=file2)
            
            if choice == '1':
                result = matrix1.add(matrix2)
                print("Addition result:")
            elif choice == '2':
                result = matrix1.subtract(matrix2)
                print("Subtraction result:")
            elif choice == '3':
                result = matrix1.multiply(matrix2)
                print("Multiplication result:")
            else:
                print("Invalid choice")
                continue
            
            print(result)
            
            # Save to file if needed
            save = input("Save result to file? (y/n): ")
            if save.lower() == 'y':
                output_file = input("Enter output file path: ")
                with open(output_file, 'w') as f:
                    f.write(f"rows={result.rows}\n")
                    f.write(f"cols={result.cols}\n")
                    for (row, col), value in result.matrix.items():
                        f.write(f"({row}, {col}, {value})\n")
                print(f"Result saved to {output_file}")
                
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()