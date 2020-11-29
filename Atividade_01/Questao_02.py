def area(raio):
    return PI * (raio ** 2)

def perimetro(raio):
    return PI * 2 * raio
    
PI = 3.14

raio = float(input('Digite o raio do círculo: '))
print(f'O valor da area do circulo é {area(raio):.2f}.')
print(f'O valor do perímetro do círculo é igual a {perimetro(raio):.2f}')
