def max(num1,num2):
    if num1 > num2:
        maior = num1
    
    elif num2 > num1:
        maior = num2

    elif num1 == num2:
        maior = num1
    
    return maior

for c in range(4):
    num1 = int(input('\nDigite um número: '))
    num2 = int(input('Digite um número: '))

    a = max(num1,num2)

    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número: '))

    b = max(num1,num2)

    print(f'O maior número digitado foi: {max(a,b)}')