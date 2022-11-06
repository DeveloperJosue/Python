### Calculadora Python 

import math 

while True: 

    novamente = '' # Para repetir a operação
    print('**********Python Calculator********** \n')

    print('''Selecione o número da operação:

    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão''')
    
    op = int(input('Digite a operação: ')) # Selecionando a opração 

    num1 = int(input('Digite o primeiro valor: '))

    num2 = int(input('Digite o segundo valor: '))

    if op == 1: # SOMA
        soma = num1 + num2 
        print(f'{num1} + {num2} = {soma}')

    elif op == 2: # SUBTRAÇÃO
        sub = num1 - num2 
        print(f'{num1} - {num2} = {sub}')

    elif op == 3: # MULTIPLICAÇÃO
        mult = num1 * num2  
        print(f'{num1} + {num2} = {mult}')

    elif op == 4: # DIVISÃO
        div = num1 / num2 
        print(f'{num1} + {num2} = {div}')

    # Pergunta para efetuar uma nova equação
    novamente = str(input('Quer efetuar uma nova operação? [S/N]')).strip().upper()[0]
    if novamente == 'N':
        break
print('FIM')