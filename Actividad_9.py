def ciclo(n):
    print(n, end=" ")

    if n == 1: 
        return
    elif n % 2 == 0:
        ciclo(n // 2)
    else: 
        ciclo(3 * n + 1)

for i in range(1, 11):
    print("Nmero inicial:",i)
    ciclo(i)
    print("\n")