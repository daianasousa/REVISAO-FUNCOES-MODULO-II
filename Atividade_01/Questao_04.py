#Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas notas por 
# parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação).

def media(n1, n2):
    return (n1 + n2) / 2

while True:
    try:
        nota1 = float(input('\nDigite sua primeira nota: '))
        nota2 = float(input('\nDigite sua segunda nota: '))

        if media(nota1, nota2) >= 6.0:
            print('\nPARABÉNS! Você foi aprovado!')
        
        else:
            print('\nQue pena! Você foi reprovado!')
        
        break
        
    except:
        print('\nDigite uma nota valida!')