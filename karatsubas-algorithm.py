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
    z_2 = karatsuba(a + b, c + d)  # ad + bc

    # combine the results into karatsubas equation
    return z_0 * 10 ** (2 * m) + ((z_2 - z_1 - z_0) * 10**m) + z_1
