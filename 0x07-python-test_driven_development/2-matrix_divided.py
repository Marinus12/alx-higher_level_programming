def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different lengths.
        TypeError: If the div is not an int or float.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix representing the result of the division.
    """

    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div, rounded to 2 decimal places
    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return result_matrix


# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
result = matrix_divided(matrix, 3)
print(result)
