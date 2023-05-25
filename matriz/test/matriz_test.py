# Import the necessary modules
import unittest
import sys
sys.path.append("matriz/model")
from matriz import generate_matrix, find_consecutive_sequence

# Define the test class that inherits from unittest.TestCase
class TestHomework(unittest.TestCase):

    # Define a test case for the generate_matrix function
    def test_generate_matrix(self):
        # Call the generate_matrix function to obtain a matrix
        matrix = generate_matrix()
    
        # Assert that the number of rows in matrix is 5
        self.assertEqual(len(matrix), 5)
        
        # Assert that the number of columns in each row is 5
        for row in matrix:
            self.assertEqual(len(row), 5)
            
            # Assert that each element in the row is between 1 and 9
            for num in row:
                self.assertTrue(1 <= num <= 9)

    # Define a test case for the find_consecutive_sequence function
    def test_find_consecutive_sequence(self):
        # Create three matrices with predetermined values for testing
        
        matrix1 = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 1],
            [2, 3, 4, 5, 6],
            [7, 8, 9, 1, 2],
            [3, 4, 5, 6, 7]
        ]
        # Assert that the function can correctly identify a horizontal sequence
        self.assertEqual(find_consecutive_sequence(matrix1), "Horizontal sequence found starting at (1, 2) and ending at (1, 5)")

        matrix2 = [
            [1, 2, 3, 4, 5],
            [5, 6, 7, 8, 9],
            [9, 8, 7, 6, 5],
            [5, 4, 3, 2, 1],
            [1, 2, 3, 4, 5]
        ]
        # Assert that the function can correctly identify a vertical sequence
        self.assertEqual(find_consecutive_sequence(matrix2), "Vertical sequence found starting at (0, 4) and ending at (3, 4)")

        matrix3 = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 1],
            [2, 3, 4, 5, 6],
            [7, 8, 9, 1, 2],
            [3, 4, 6, 6, 7]
        ]
        # Assert that the function returns "No consecutive sequence found" for a matrix without sequences
        self.assertEqual(find_consecutive_sequence(matrix3), "No consecutive sequence found")
        
# Run the test suite if the script is run directly
if __name__ == '__main__':
    unittest.main()
