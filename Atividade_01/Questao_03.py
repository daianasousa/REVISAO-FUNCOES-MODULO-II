#Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar o valor correspondente em graus Celsius. 
# Fórmula: C = ((F-32)/9)*5

def celsius(f):
    return ((f - 32) / 9) * 5

f = float(input('Digite uma temperatura em graus Fahrenheit: '))

print(f'A temperatura {f:.1f}°F equivale a {celsius(f):.1f}°C.')