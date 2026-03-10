def multiplicar_matrices(A, B):
    filas_A = len(A)
    columnas_A = len(A[0])
    columnas_B = len(B[0])

    resultado = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]

    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                resultado[i][j] += A[i][k] * B[k][j]

    return resultado

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print(multiplicar_matrices(A, B))