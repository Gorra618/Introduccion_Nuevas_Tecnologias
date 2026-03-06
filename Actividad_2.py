def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def n_primo(n):
    contador = 0
    numero = 1
    while contador < n:
        numero += 1
        if es_primo(numero):
            contador += 1
    return numero

print(n_primo(6))  
