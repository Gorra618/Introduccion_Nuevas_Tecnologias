def ciclo(n):
    print("Inicio:", n)

    while n != 1:
        if n % 2 == 0:  
            n = n // 2
        else:            
            n = 3 * n + 1
        
        print(n)


for i in range(1, 11):
    print("Numero inicial:", i)
    ciclo(i)
    print()