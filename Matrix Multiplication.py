r1 = int(input("Enter number of rows for Matrix A: "))
c1 = int(input("Enter number of columns for Matrix A: "))
r2 = int(input("Enter number of rows for Matrix B: "))
c2 = int(input("Enter number of columns for Matrix B: "))
if c1 != r2:
    print("Matrix multiplication not possible!")
else:
    print("Enter Matrix A:")
    A = [[int(input()) for _ in range(c1)] for _ in range(r1)]

    print("Enter Matrix B:")
    B = [[int(input()) for _ in range(c2)] for _ in range(r2)]

    result = [[0 for _ in range(c2)] for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    print("Resultant Matrix:")
    for row in result:
        print(row)
