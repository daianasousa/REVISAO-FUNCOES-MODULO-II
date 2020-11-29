def divisores(numero):
    cont = 0
    for a in range(1,numero+1):
        if numero % a == 0:
            cont += 1
    
    return cont

numero = int(input('Digite um número inteiro positivo: '))
print(f'O numero {numero}, tem {divisores(numero)} divisores.')