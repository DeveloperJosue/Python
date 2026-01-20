timej = list()
jogador = dict()
partidas = list()

import time 

# Cadastro de jogadores
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()

# Registro de gols por partida
    for c in range(0, tot): 
        partidas.append(int(input(f'   Quantos gols na partidas {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    timej.append(jogador.copy())

# Continuação do cadastro
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break 
        print('ERRO! Responda Apenas S ou N')
    if resp == 'N':
        break

time.sleep(0.3)
print('Cadastro finalizado!')
time.sleep(0.5)

# Exibição do relatório
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f' {i:<15}', end='')
print()
print('-' * 40)
for k,v in enumerate(timej):
    print(f' {k:>3}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('-' * 40)

# Consulta detalhada de desempenho dos jogadores
while True:
    try:
        busca = int(input('Mostrar dados de qual jogador (99 exit) '))
    except ValueError:
        print('ERRO! Digite o COD do jogador.')      #Tratamento de erro para entrada inválida
        continue
    if busca == 99:
        break                                    # Sair do loop
    if busca >= len(timej):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {timej[busca] ["nome"]}: ')
        for i, g in enumerate(timej[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<<VOLTE SEMPRE>>')