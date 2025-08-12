def karatsuba(x, y):
    # Base case: if single digits return product directly
    if x < 10 or y < 10:
        return x * y

    # Calculate the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split the digit sequences in the middle
    # // 10**m for high part, % 10**m for low part
    a = x // 10**m
    b = x % 10**m
    c = y // 10**m
    d = y % 10**m

    # 3 recursive calls to the Karatsuba algorithm
    z_0 = karatsuba(a, c)  # ac
    z_1 = karatsuba(b, d)  # bd
    z_2 = karatsuba(a + b, c + d)  # (a+b)(c+d)

    # combine the results into karatsubas equation
    return z_0 * 10 ** (2 * m) + ((z_2 - z_1 - z_0) * 10**m) + z_1


# Test script to demonstrate the karatsuba function
if __name__ == "__main__":

    # assigning large 64 digit numbers for testing
    num1 = 3141592653589793238462643383279502884197169399375105820974944592
    num2 = 2718281828459045235360287471352662497757247093699959574966967627

    # assigning test cases
    test_cases = [
        (1234, 5678),
        (123456789, 987654321),
        (0, 1234),
        (1234, 0),
        (num1, num2),
    ]

print("-----Karatsuba Multiplication Results-----")

# Compare results with Python's built-in multiplication
for x, y in test_cases:
    result = karatsuba(x, y)
    python_version = x * y  # Python's built-in multiplication for comparison

    print(f"Testing {x} * {y}:")

    print(f"Karatsuba result: {result}")
    print(f"Python result: {python_version}")

    if result == python_version:
        print("PASS ✅\n")
    else:
        print("FAIL ❌\n")
