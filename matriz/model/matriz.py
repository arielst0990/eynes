import random

def generate_matrix():
    matrix = []
    for _ in range(5):
        row = [random.randint(1, 9) for _ in range(5)]
        matrix.append(row)
    return matrix

def find_consecutive_sequence(matrix):
    # Check horizontal sequences
    for i in range(5):
        for j in range(2):
            if matrix[i][j] == matrix[i][j+1] == matrix[i][j+2] == matrix[i][j+3]:
                return f"Horizontal sequence found starting at ({i}, {j}) and ending at ({i}, {j+3})"
    
    # Check vertical sequences
    for i in range(2):
        for j in range(5):
            if matrix[i][j] == matrix[i+1][j] == matrix[i+2][j] == matrix[i+3][j]:
                return f"Vertical sequence found starting at ({i}, {j}) and ending at ({i+3}, {j})"
    
    return "No consecutive sequence found"

# Generate the matrix
matrix = generate_matrix()

# Print the matrix
for row in matrix:
    print(row)

# Find consecutive sequence
result = find_consecutive_sequence(matrix)
print(result)
