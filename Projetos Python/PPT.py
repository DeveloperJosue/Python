from random import randint
import time

print('-='*10)
print('Vamos Jogar Jokenpô')
print('-='*10)
time.sleep(1)

nome = str(input('Nome do Jogador: '))
time.sleep(0.5)

contV, contE, contD  = 0, 0, 0   #Contadores de Vitórias, Empates e Derrotas

while True:
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)

    print('''Suas Opções de Jogo:
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura ''')
    time.sleep(0.5)

    jogador = int(input('Qual é sua Jogada: '))

    if jogador < 0 or jogador > 2 or jogador == '00':
        print('Jogada INVÁLIDA!! Tente Novamente. ')
        continue

    time.sleep(0.5)
    print('Vamos Lá')
    time.sleep(0.5)
    print('Jo')
    time.sleep(0.5)
    print('Ken')
    time.sleep(0.5)
    print('Pô')
    time.sleep(0.5)

#Momento da jogada

    print('-='*15)
    print(f'Computador Jogou {itens[computador]}')
    time.sleep(0.5)
    print(f'Você Jogou {itens[jogador]}')
    print('-='*15)

#Computador Jogou Pedra

    if computador == 0:   
        if jogador == 0:
            print('Empate!!')
            contE += 1
        elif jogador == 1:
            print('Você Venceu!!')
            contV += 1
        elif jogador == 2:
            print('Você Perdeu!!')
            contD += 1
        else:
            print('Jogada INVÁLIDA!! Tente Novamente. ')

#Computador Jogou Papel

    elif computador == 1:   
        if jogador == 0:
            print('Você Perdeu!!')
            contD += 1
        elif jogador == 1:
            print('Empate!!')
            contE += 1
        elif jogador == 2:
            print('Você Ganhou!!')
            contV += 1
        else:
            print('Jogada INVÁLIDA!! Tente Novamente. ')

#Computador Jogou Tesoura

    elif computador == 2:   
        if jogador == 0:
            print('Você Ganhou!!')
            contV += 1
        elif jogador == 1:
            print('Você Perdeu!!')
            contD += 1
        elif jogador == 2:
            print('Empate')
            contE += 1
        else:
            print('Jogada INVÁLIDA!! Tente Novamente. ')

#Reinício do Jogo ou finalização 

    novamente = str(input('Quer jogar novamente[S/N]: ')).strip().upper() [0]
    if novamente == 'N':
        break 

#Finalização do Jogo

time.sleep(1) 
print('-='*15)
print(f'''Seu resumo da partida: 
    Vitórias: {contV} vezes;
    Derrotas: {contD} vezes;
    Empates:  {contE} vezes.
    Com o total de {contV + contD + contE} partidas.''') # Contagem Final
print('-='*15)
time.sleep(3)
print(f'FIM DO JOGO! Obrigado por jogar {nome}.')