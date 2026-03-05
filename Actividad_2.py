n = 1

def es_primo(n):
    if n <= 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

if es_primo(n):
    for i in
else:
    print("No es un primo, no se hace realiza la operación")