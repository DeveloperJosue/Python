from random import randint
import time

print('-='*10)
print('Vamos Jogar Jokenpô')
print('-='*10)
time.sleep(1)

nome = str(input('Nome do Jogador: '))
time.sleep(1)

while True:
    cont = 0
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)

    print('''Suas Opções de Jogo:
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura ''')
    time.sleep(1)

    jogador = int(input('Qual é sua Jogada: '))
    time.sleep(0.5)
    print('Vamos Lá')
    time.sleep(0.5)
    print('Jo')
    time.sleep(0.5)
    print('Ken')
    time.sleep(0.5)
    print('Pô')
    time.sleep(0.5)

    print('-='*10)
    print(f'Computador Jogou {itens[computador]}')
    time.sleep(0.5)
    print(f'Você Jogou {itens[jogador]}')
    print('-='*10)

    if computador == 0:   #Computador Jogou Pedra
        if jogador == 0:
            print('Empate!!')
        elif jogador == 1:
            print('Você Venceu!!')
            cont =+1
        elif jogador == 2:
            print('Você Perdeu!!')
        else:
            print('Jogada INVÁLIDA!! Tente Novamente. ')

    elif computador == 1:   #Computador Jogou Papel
        if jogador == 0:
            print('Você Perdeu!!')
        elif jogador == 1:
            print('Empate!!')
        elif jogador == 2:
            print('Você Ganhou!!')
            cont =+1
        else:
            print('Jogada INVÁLIDA!! Tente Novamente. ')

    elif computador == 2:   #Computador Jogou Tesoura
        if jogador == 0:
            print('Você Ganhou!!')
            cont =+1
        elif jogador == 1:
            print('Você Perdeu!!')
        elif jogador == 2:
            print('Empate')
        else:
            print('Jogada INVÁLIDA!! Tente Novamente. ')
    
    novamente = str(input('Quer jogar novamente[S/N]: ')).strip().upper() [0]
    if novamente == 'N':
        break 
    time.sleep(1)
print('-='*10)
print(f'Você ganhou {cont} vezes.')
time.sleep(1)
print(f'FIM DO JOGO! Obrigado por jogar {nome}.')