from random import randint
import time 
v = 0
titulo = 'Vamos Jogar Par ou Impar'
print(f'\033[34m{titulo:-^50}\033[m')
time.sleep(1)
nome = str(input('Qual é seu nome: '))
print(f'Então Vamos lá {nome}!!')
time.sleep(0.5)
while True:
    novamente = ' '
    while True:
        jogador = int(input('Digite um valor até 9: '))
        computador = randint(0, 10)
        total = jogador + computador 
        tipo = ' '
        while tipo not in 'PI':
            tipo = str(input('Par ou Impar?[P/I]: ')).strip().upper() [0]
        print('Vamos Lá')
        time.sleep(1)
        print('\033[31m1')
        time.sleep(0.5)
        print('2')
        time.sleep(0.5)
        print('3\033[m')
        time.sleep(0.5)
        print(f'Você  jogou {jogador} e o computador {computador}. Tendo total de {total}.')
        time.sleep(1)
        print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR' )
        if tipo == 'P':
            if total % 2 == 0:
                print('\033[33mVOCÊ VENCEU!! \033[m')
                v += 1
            else:
                print('\033[31mVOCÊ PERDEU\033[m')
                break
        elif tipo == 'I':
            if total % 2 == 1:
                print('\033[33mVOCÊ VENCEU!! \033[m')
                v += 1
            else:
                print('\033[31mVOCÊ PERDEU\033[m')
                break
        print('Vamos Jogar Novamente ...')
    print(f'GAMER OVER!! Você venceu {v} vezes!!.')
    novamente = str(input('Quer jogar novamente[S/N]: ')).strip().upper() [0]
    if novamente == 'N':
        break 
print(f'FIM DO JOGO! Obrigado por jogar {nome}.')