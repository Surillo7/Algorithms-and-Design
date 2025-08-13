import numpy as np


# Multiplies two matrices A and B using Strassen's algorithm.
# A and B must be square matrices of the same size.
def strassen(A, B):
    # Base case: if the matrix is 1x1
    if len(A) == 1:
        return A * B

    # Split matrices into quadrants using NumPy's array slicing
    n = len(A)
    mid = n // 2
    a11, a12, a21, a22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
    b11, b12, b21, b22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]

    # Calculate the 7 products recursively.
    # Notice we can just use '+' and '-' for matrix math!
    p1 = strassen(a11 + a22, b11 + b22)
    p2 = strassen(a21 + a22, b11)
    p3 = strassen(a11, b12 - b22)
    p4 = strassen(a22, b21 - b11)
    p5 = strassen(a11 + a12, b22)
    p6 = strassen(a21 - a11, b11 + b12)
    p7 = strassen(a12 - a22, b21 + b22)

    # Combine the products to get the result quadrants
    c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5
    c21 = p2 + p4
    c22 = p1 - p2 + p3 + p6

    # Assemble the final matrix from the quadrants using np.vstack and np.hstack
    # vstack = vertical stack, hstack = horizontal stack
    C = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

    return C


# Test script to demonstrate Strassen's algorithm
if __name__ == "__main__":
    # Example matrices for testing
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    # Perform Strassen's multiplication
    result = strassen(A, B)

    print("-----Strassen's Algorithm Results-----")
    print("Matrix A:")
    print(A)
    print("Matrix B:")
    print(B)
    print("Result of Strassen's multiplication:")
    print(result)
